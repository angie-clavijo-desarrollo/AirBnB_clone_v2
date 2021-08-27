#!/usr/bin/python3
""" Fabric for create a local pack with web static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function pack"""
    try:
        local("mkdir -p versions")
        format_file = "versions/web_static_{}.tgz".format(datetime.now())
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except as e:
        return None
