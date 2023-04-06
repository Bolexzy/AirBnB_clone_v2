#!/usr/bin/env bash
""" Fabric script that generates a .tgz archive
from the contents of the web_static folder"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Creates a gzipped tar archive from the web_static/ content"""
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        now = datetime.now()
        ft = now.strftime("%Y%m%d%H%M%S")
        archive_path = f"versions/web_static_{ft}.tgz"
        local(f"tar -cvzf {archive_path}  web_static/")
        return archive_path
    except Exception as e:
        print(f"An exception occurred: {e}")
        return None