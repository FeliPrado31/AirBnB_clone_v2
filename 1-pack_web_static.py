#!/usr/bin/python3
# Write a Fabric script (based on the file 2-do_deploy_web_static.py)
# that creates and distributes an archive to your web servers
# using the function deploy:

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """
    Generate file
    """
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir("versions") is False:
           local("mkdir versions")
        f = 'versions/web_static_' + time + '.tgz'
        local('tar -vzcf {} web_static'.format(f))
        return f
    except:
        return None
