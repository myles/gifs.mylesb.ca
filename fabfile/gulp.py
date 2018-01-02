# -*- coding: utf-8 -*-
"""Fabric Gulp Commands and Wrapper."""
from fabric.api import local, task
from fabric.context_managers import shell_env


def gulp(command, *args, **kwargs):
    """Gulp command line wrapper."""
    opts = []

    for arg in args:
        opts.append('--{}'.format(arg))

    for key, value in kwargs.items():
        opts.append('--{0}={1}'.format(key, value))

    with shell_env(NODE_ENV='production'):
        local('./node_modules/.bin/gulp {0} {1}'.format(command,
                                                        ' '.join(opts)))


@task
def build():
    """Build the websites static assets."""
    gulp('build')
