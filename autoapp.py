# -*- coding: utf-8 -*-
"""Create an application instance."""
from web.app import create_app
from web.config import Config

app = create_app(Config)
