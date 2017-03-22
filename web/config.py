# -*- coding: utf-8 -*-
"""Application configuration."""
import re
from os import pardir
from os.path import abspath, dirname, join


class Config(object):
    DEBUG = True

    # GitHub Repository URL
    GITHUB_REPO = 'https://github.com/myles/talks'

    # Paths
    APP_PATH = dirname(abspath(__file__))
    ROOT_PATH = abspath(join(APP_PATH, pardir))

    STATIC_PATH = join(APP_PATH, 'static')

    GIFS_PATH = join(ROOT_PATH, 'gifs')

    # Regexs
    GIF_REGEX = re.compile(r'^.*/gifs/(?P<name>[/.a-zA-Z0-9-_]+).gif$')

    # Frozen-Flask Config
    # FREEZER_STATIC_IGNORE = ()
    FREEZER_DESTINATION = join(ROOT_PATH, 'build')
