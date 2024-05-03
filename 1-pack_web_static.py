#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    generates a .tgz archive from the
    contents of the web_static folder of
    your AirBnB Clone repo
    """
    now = datetime.now()
    file_name = f"web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}"
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/{file_name} web_static")
    path = f"versions/{file_name}.tgz"
    if result.succeeded:
        return path
    else:
        return None
