#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import subprocess
import mydblib as db
import rrdtool
import tempfile
import os

RRDFILE = "gyro.rrd"
STATIC_SERVE="http://12.168.83.99:9999"

html = """
<html>
<body>
   <form method="get" action="">
        <p>
           Bash command: <input type="text" name="cmd" value="%(cmd)s" size="100">
        </p>
        <p>
            Retrieve info:
            <input
                name="infos" type="checkbox" value="gyroscope"
                %(checked-gyroscope)s
            > Gyroscope
            <input
                name="infos" type="checkbox" value="cpu"
                %(checked-cpu)s
            > CPU
            <input
                name="infos" type="checkbox" value="network"
                %(checked-network)s
            > Network
        </p>
        <p>
           Update gyroscope sample time (tenth of seconds): <input type="text" name="setup_gyro_seconds" value="%(gyro_seconds)s">
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>Requested: %(infos_str)s</p>
    %(answers_html)s
</body>
</html>
"""


def my_shell_exec(cmd):
    try:
        rv = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        rv = "[ERROR %s] command=%s, output=\n%s" % (e.returncode, e.cmd,
                                                     e.output)
    return rv


def get_gyroscope_graph():

    HOUR = 3600
    fd, path = tempfile.mkstemp('.png')

    rrdtool.graph(path,
                  '--imgformat',
                  'PNG',
                  '--width',
                  '640',
                  '--height',
                  '300',
                  '--start',
                  "-%i" % HOUR,
                  '--end',
                  "-1",
                  '--vertical-label',
                  'Gyroscope values',
                  '--title',
                  'Hourly gyroscope',
                  'DEF:x=%s:x:AVERAGE' % RRDFILE,
                  'DEF:y=%s:y:AVERAGE' % RRDFILE,
                  'DEF:z=%s:z:AVERAGE' % RRDFILE,
                  'DEF:rx=%s:rx:AVERAGE' % RRDFILE,
                  'DEF:ry=%s:ry:AVERAGE' % RRDFILE,
                  'DEF:rz=%s:rz:AVERAGE' % RRDFILE,
                  'LINE:x#990033:X axis',
                  'LINE:y#339900:Y axis',
                  'LINE:z#003399:Z axis',
                  'LINE:rx#999933:X rotation',
                  'LINE:ry#339999:Y rotation',
                  'LINE:rz#993399:Z rotation', )

    return path


def application(environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    cmd = d.get('cmd', [''])[0]  # Returns the first cmd value
    infos = d.get('infos', [])  # Returns a list of info

    gyro_seconds = int(db.get_setup_option('gyro_seconds'))
    new_gyro_seconds = d.get('setup_gyro_seconds', [''])[0]

    # Always escape user input to avoid script injection
    answers = {}
    if cmd:
        answers[cmd] = my_shell_exec(cmd)

    if "cpu" in infos:
        answers["cpu"] = my_shell_exec("/usr/bin/lscpu")
    if "network" in infos:
        answers["ip"] = my_shell_exec("/sbin/ip addr list")
        answers["route"] = my_shell_exec("/sbin/ip route")
    if "gyroscope" in infos:
        answers["gyroscope"] = get_gyroscope_graph()
    if new_gyro_seconds:
        try:  # sanitize
            new_gyro_seconds = int(new_gyro_seconds)
        except:
            answers[
                "update gyroscope sample time"] = "ValueError (%s) you have to provide an integer value" % new_gyro_seconds
        else:
            if new_gyro_seconds != gyro_seconds:
                try:
                    db.set_setup_option('gyro_seconds', new_gyro_seconds)
                except:
                    answers[
                        "update gyroscope sample time"] = "Error in db update for gyro_seconds"
                else:
                    answers[
                        "update gyroscope sample time"] = "Updated gyroscope sample to %s seconds" % (new_gyro_seconds/10)
                    gyro_seconds = new_gyro_seconds

    answers_html = ""
    for key, value in answers.items():
        answers_html += "<h2>%s</h2>" % escape(key)
        if key == "gyroscope":
            answers_html += '<img src="%s/%s" />' % (STATIC_SERVE, os.path.basename(
                value))
        else:
            answers_html += "<pre>%s</pre>" % escape(value)

    info_str = "<ul>"
    for x in [cmd] + infos:
        info_str += "<li>%s</li>" % x
    info_str += "</ul>"
    response_body = html % {  # Fill the above html template in
        'checked-cpu': ('', 'checked')['cpu' in infos],
        'checked-network': ('', 'checked')['network' in infos],
        'checked-gyroscope': ('', 'checked')['gyroscope' in infos],
        'answers_html': answers_html,
        'infos_str': info_str,
        'cmd': escape(cmd),
        'gyro_seconds': gyro_seconds,
    }

    status = '200 OK'

    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]


httpd = make_server('0.0.0.0', 8051, application)

# Now it is serve_forever() in instead of handle_request()
httpd.serve_forever()
