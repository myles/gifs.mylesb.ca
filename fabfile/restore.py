# -*- coding: utf-8 -*-
"""Fabric restore from remote tasks."""
import fnmatch
import os

from fabric.api import env, task, local

from . import config, rsync  # noqa: F401


@task
def main():
    """Restore gifs from backup."""
    # rsync.pull()

    build_dir = os.path.join(env.root_dir, 'build')
    gifs_dir = os.path.join(env.root_dir, 'gifs')

    gif_files = []

    for root, dirnames, filenames in os.walk(build_dir):
        for filename in fnmatch.filter(filenames, '*.gif'):
            gif_files.append(os.path.join(root, filename))

        for filename in fnmatch.filter(filenames, '*.mp4'):
            gif_files.append(os.path.join(root, filename))

    for old_gif_file in gif_files:
        new_gif_file = old_gif_file.replace(build_dir + '/', '')
        new_gif_file = new_gif_file.replace('/image', '')

        new_gif_file = os.path.join(gifs_dir, new_gif_file)

        if not os.path.exists(os.path.dirname(new_gif_file)):
            os.makedirs(os.path.dirname(new_gif_file))

        local('cp {0} {1}'.format(old_gif_file, new_gif_file))
