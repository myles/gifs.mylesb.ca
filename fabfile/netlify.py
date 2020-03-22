# -*- coding: utf-8 -*-
"""Fabric rsync Tasks."""
from fabric.api import env, local, task


@task
def push():
    """Push website though rsync."""
    local('netlify deploy --prod --dir={build_dir}/'.format(**dict(env)))
