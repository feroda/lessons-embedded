import sqlite3
DBNAME = "sysconfig.sqlite"


def get_setup_option(optname):
    dbconn = sqlite3.connect(DBNAME)
    cu = dbconn.cursor()
    cu.execute("SELECT value FROM setup WHERE key=?", (optname, ))
    optvalue = cu.fetchone()[0]
    dbconn.close()
    return optvalue


def set_setup_option(optname, optvalue):
    dbconn = sqlite3.connect(DBNAME)
    cu = dbconn.cursor()
    # NEVER DO THIS! IS INSECURE: cu.execute("UPDATE setup SET value=%s where key=%s" % (optvalue, optname))
    # DO THIS
    cu.execute("UPDATE setup SET value=? where key=?", (optvalue, optname))
    dbconn.commit()
    dbconn.close()
    return True
