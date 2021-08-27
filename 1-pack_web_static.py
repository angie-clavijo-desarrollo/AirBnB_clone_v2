#!/usr/bin/python3
""" Fabric for create a
    local pack with web static """
from fabric.api import *
from os import path
from datetime import datetime


def do_pack():
    """ Function pack """
    x = datetime.now().strftime("%Y%m%d%H%M%S")

    if not path.exists("./versions"):
        local("sudo mkdir -p versions")

    format_file = "versions/web_static_{}.tgz".format(x)
    try:
        local("sudo tar -cvzf {} web_static").format(format_file)
        return(format_file)
    except Exception as exception:
        return(None)
