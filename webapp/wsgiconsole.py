#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import subprocess

html = """
<html>
<body onload="setTimeout('window.location.reload();', 2000);">
   <form method="get" action="">
        <p>
           Bash command: <input type="text" name="cmd" value="%(cmd)s" size="200">
        </p>
        <p>
            Retrieve info:
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
            <input type="submit" value="Submit">
        </p>
    </form>
    <p>Requested: %(infos_str)s</p>
    %(answers_html)s

</body>
</html>
"""


def application(environ, start_response):

    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # As there can be more than one value for a variable then
    # a list is provided as a default value.
    cmd = d.get('cmd', [''])[0]  # Returns the first cmd value
    infos = d.get('infos', [])  # Returns a list of info

    # Always escape user input to avoid script injection
    answers = {}
    if cmd:
        answers[cmd] = subprocess.check_output(cmd, shell=True)

    if "cpu" in infos:
        answers["cpu"] = subprocess.check_output("/usr/bin/lscpu", shell=True)
    if "network" in infos:
        answers["ip"] = subprocess.check_output("/usr/bin/ip addr list",
                                                shell=True)
        answers["route"] = subprocess.check_output("/usr/bin/ip route",
                                                   shell=True)

    answers_html = ""
    for key, value in answers.items():
        answers_html += "<h2>%s</h2><pre>%s</pre>" % (escape(key),
                                                      escape(value))

    response_body = html % {  # Fill the above html template in
        'checked-cpu': ('', 'checked')['cpu' in infos],
        'checked-network': ('', 'checked')['network' in infos],
        'answers_html': answers_html,
        'infos_str': " ".join([cmd] + infos),
        'cmd': escape(cmd)
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
