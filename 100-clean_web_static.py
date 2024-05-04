#!/usr/bin/python3
"""
Deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['52.87.230.55', '100.25.150.51']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    number = int(number)
    if number == 0:
        number = 1

    with cd('/data/web_static/releases/'):
        releases = sorted(run('ls -tr').split())
        print('releases:', releases)
        deletes = releases[:-number]
        for release in releases:
            if release in deletes and release.startswith('web_static_'):
                run(f"sudo rm -rf {release}")

    local_archs = sorted(os.listdir('versions'))
    print("Local Archives:", local_archs)
    deletes = local_archs[:-number]
    for arch in local_archs:
        if arch in deletes and arch.startswith('web_static_'):
            local(f"sudo rm -rf versions/{arch}")
