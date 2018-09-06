# -*- coding: utf-8 -*-
"""Fabfile."""
from fabric.api import task

from . import config, flaskcli, gulp, giphy, netlify, restore, rsync


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
    # rsync.push()
    netlify.push()


@task
def runserver():
    """Run a test web server locally."""
    gulp.build()
    flaskcli.run()
