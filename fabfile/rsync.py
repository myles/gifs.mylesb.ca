# -*- coding: utf-8 -*-
"""Fabric rsync Tasks."""
from fabric.api import env, local, task


@task
def push():
    """Push website though rsync."""
    local('rsync -pthrvz {build_dir}/ {remote}'.format(**dict(env)))


@task
def pull():
    """Pull gifs from remote."""
    local('rsync -pthrvz {remote} {build_dir}'.format(**dict(env)))
