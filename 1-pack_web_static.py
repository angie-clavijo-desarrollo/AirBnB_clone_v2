#!/usr/bin/python3
""" Fabric for create a
    local pack with web static """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function pack """
    x = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    format_file = "versions/web_static_{}.tgz".format(x)
    try:
        local("tar -czvf " + format_file + " web_static")
        return(format_file)
    except Exception as exception:
        return(None)
