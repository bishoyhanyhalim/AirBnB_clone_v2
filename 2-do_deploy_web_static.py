#!/usr/bin/python3
"""
A Fabric script  that distributes
an archive to web servers
"""

from fabric.api import local, run, env, put
import os.path

env.hosts = ['52.87.230.55', '100.25.150.51']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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
