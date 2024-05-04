#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['18.208.120.216', '100.25.110.24']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder of
    your AirBnB Clone repo
    """
    now = datetime.now()
    file_name = (
        f"web_static_{now.year}{now.month}"
        f"{now.day}{now.hour}{now.minute}{now.second}.tgz"
    )
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{file_name} web_static")
    path = f"versions/{file_name}.tgz"
    if result.succeeded:
        return path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False

    archive = archive_path.split('/')[-1]
    folder = archive.split('.')[0]
    deploy_path = "/data/web_static/releases/"
    tmp_path = "/tmp/"

    if put(archive_path, tmp_path).failed is True:
        return False
    if run(f"mkdir -p {deploy_path}{folder}").failed is True:
        return False
    if run(f"tar -xzf {tmp_path}{archive} -C {deploy_path}{folder}").failed:
        return False
    if run(f"rm {tmp_path}{archive}").failed is True:
        return False
    if run(f"mv {deploy_path}{folder}/web_static/* "
           f"{deploy_path}{folder}").failed:
        return False
    if run(f"rm -rf {deploy_path}{folder}/web_static").failed:
        return False
    if run(f"rm -rf /data/web_static/current").failed:
        return False
    if run(f"ln -s {deploy_path}{folder}/ /data/web_static/current").failed:
        return False
    print("New version deployed!")
    return True


def deploy():
    """
    Deploys the archive to web servers
    """
    archive = do_pack()
    if archive is None:
        return False
    res = do_deploy(archive_path=archive)
    return res
