# -*- coding: utf-8 -*-
"""Fabfile."""
from fabric.api import task

from . import config, flaskcli, rsync  # noqa: F401


@task
def build():
    """Builds the website."""
    flaskcli.freeze()


@task
def deploy():
    """Deploy the website."""
    flaskcli.freeze()
    rsync.push()


@task
def develop():
    """Run a test web server locally."""
    flaskcli.run()
