#!/usr/bin/python3
""" Comment"""
from fabric.api import local, put, run, env
from datetime import datetime

env.hosts = ['ubuntu@54.242.180.91','ubuntu@35.229.117.230']


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


def do_deploy(archive_path):
    """ Deploy archives at server"""
    request_tgz = archive_path.split("/")[-1]
    resource_path = "/data/web_static/releases/{}/".format(request_tgz[:-4])
    dir_server = "/tmp/{}".format(request_tgz)

    if not archive_path:
        return(False)

    try:
        # upload tgz at servers
        upload = put(archive_path, "/tmp/")

        # folder at uncompressed tgz files
        run("mkdir -p {}".format(resource_path))

        # uncompresses files
        run("tar -xzf {} -C {}".format(dir_server, resource_path))

        # remove dir of files tgz
        run("rm {}".format(dir_server))

        # move files compresses
        run("mv {}web_static/* {}".format(resource_path, resource_path))

        # remove dir
        run("rm -rf {}/web_static".format(resource_path))

        # delete symbolic link
        run("rm -rf /data/web_static/current")

        # create new symbolic link
        run("ln -s {} /data/web_static/current".format(resource_path))
        return(True)

    except as e:
        return(False)
