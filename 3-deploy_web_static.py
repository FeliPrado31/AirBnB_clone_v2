#!/usr/bin/python3
# This fabscript deploys the web static content
from os import path
from fabric.api import sudo, env, put, local
from datetime import datetime

env.hosts = ["35.243.229.224", "34.229.175.198"]


def do_pack():
    """
    Generate file
    """
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir("versions") is False:
            local("mkdir versions")
        f = 'versions/web_static_' + time + '.tgz'
        local('tar -cvzf {} web_static'.format(f))
        return f
    except:
        return None


def do_deploy(archive_path):
    """ simple func """

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


def deploy():
    """
    This function do a full deployment
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
