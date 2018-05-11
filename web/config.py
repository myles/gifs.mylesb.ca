# -*- coding: utf-8 -*-
"""Application configuration."""
import re
from os import environ, pardir
from os.path import abspath, dirname, join


class Config(object):
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0

    # URL
    URL = 'https://gifs.mylesb.ca/'
    URL_TPL = 'https://gifs.mylesb.ca/{}'

    # GitHub Repository URL
    GITHUB_REPO = 'https://github.com/myles/gifs.mylesb.ca'

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

    # Algolia
    ALGOLIA_APP_ID = environ.get('ALGOLIA_APP_ID')
    ALGOLIA_API_KEY = environ.get('ALGOLIA_API_KEY')
    ALGOLIA_INDEX_NAME = environ.get('ALGOLIA_INDEX_NAME')
