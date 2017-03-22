# -*- coding: utf-8 -*-
"""Click commands."""
import click

from flask import current_app
from flask.cli import with_appcontext
from flask_frozen import Freezer


@click.command()
@with_appcontext
def freeze():
    freezer = Freezer(current_app)
    freezer.freeze()
