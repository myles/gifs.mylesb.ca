# -*- coding: utf-8 -*-
"""The app module."""
from flask import Flask

from web import commands
from web.views import blueprint


def create_app(config='web.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config)

    app.cli.add_command(commands.freeze)

    app.register_blueprint(blueprint)

    return app
