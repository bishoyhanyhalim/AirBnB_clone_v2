#!/usr/bin/python3
"""
this is task 3
"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['52.87.230.55', '100.25.150.51']
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
    path = f"versions/{file_name}"
    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        archive = archive_path.split('/')[-1]
        folder = archive.split('.')[0]
        deploy_path = "/data/web_static/releases/"
        tmp_path = "/tmp/"

        put(archive_path, tmp_path)
        run(f"mkdir -p {deploy_path}{folder}/")
        run(f"tar -xzf {tmp_path}{archive} -C {deploy_path}{folder}/")
        run(f"rm {tmp_path}{archive}")
        run(f"mv {deploy_path}{folder}/web_static/* {deploy_path}{folder}/")
        run(f"rm -rf {deploy_path}{folder}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {deploy_path}{folder}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Deploys the archive to web servers
    """
    archive = do_pack()
    if archive is None:
        return False
    res = do_deploy(archive_path=archive)
    return res
