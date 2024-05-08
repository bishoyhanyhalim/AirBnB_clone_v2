#!/usr/bin/python3
"""Fabric script for task 2"""

import os.path
from fabric.api import *

env.hosts = ['54.175.199.26', '107.23.117.21']


def do_deploy(archive_path):
    """this func for task 2"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        full_path = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(full_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, full_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(full_path, full_path))
        run("rm -rf {}web_static".format(full_path))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(full_path, symlink))
        return True
    except Exception:
        return False
