# -*- coding: utf-8 -*-
"""The app module."""
import datetime

from flask import Flask

from web import commands
from web.views import blueprint


def create_app(config='web.config.Config'):
    app = Flask(__name__)

    app.config.from_object(config)

    app.cli.add_command(commands.freeze)

    app.register_blueprint(blueprint)

    @app.context_processor
    def date_processor():
        def now(strftime='%Y-%m-%dT%H:%M:%S'):
            return datetime.datetime.now().strftime(strftime)

        return dict(now=now)

    return app
