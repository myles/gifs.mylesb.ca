# -*- coding: utf-8 -*-
"""Fabfile."""
from fabric.api import task

from . import config, flaskcli, gulp, giphy, restore, rsync  # noqa: F401


@task
def build():
    """Builds the website."""
    gulp.build()
    flaskcli.freeze()


@task
def deploy():
    """Deploy the website."""
    gulp.build()
    flaskcli.freeze()
    rsync.push()


@task
def develop():
    """Run a test web server locally."""
    gulp.build()
    flaskcli.run()
