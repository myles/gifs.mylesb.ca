# -*- coding: utf-8 -*-
"""Fabric Flask Commands and Wrapper."""
from fabric.api import local, task


def flask(command, *args, **kwargs):
    """Flask command line wrapper."""
    opts = []

    for arg in args:
        opts.append('--{0}'.format(arg))

    for key, value in kwargs.items():
        opts.append('--{0}={1}'.format(key, value))

    local('pipenv run flask {0} {1}'.format(command, ' '.join(opts)))


@task
def freeze():
    """Freeze the website."""
    flask('freeze')


@task
def run():
    """Runs a development server."""
    flask('run')
