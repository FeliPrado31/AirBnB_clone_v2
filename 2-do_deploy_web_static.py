#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
using the function do_deploy:
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['35.227.104.194', '52.201.243.73']

if exists(archive_path) is False:
    return False

    try:
        # split
        f = archive_path.split("/")[-1]
        name = f.split(".")[0]
        # get full route
        path = "/data/web_static/releases/"
        # call the commands
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f, path, name))
        run('rm /tmp/{}'.format(f))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))
        return True
    except:
        return False
