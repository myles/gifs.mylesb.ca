# -*- coding: utf-8 -*-
"""Fabric rsync Tasks."""
from fabric.api import env, local, task


@task
def push(environment='stag'):
    """Push website though rsync."""
    local('rsync -pthrvz {build_dir}/ {remote}'.format(**dict(env)))


@task
def pull(environment='stag'):
    """Pull gifs from remote."""
    local('rsync -pthrvz {remote} {build_dir}'.format(**dict(env)))
