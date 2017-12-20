# -*- coding: utf-8 -*-
"""Get Fabric Configuration."""
from os import pardir, environ
from os.path import abspath, dirname, join, realpath

from dotenv import load_dotenv, find_dotenv
from fabric.api import env

load_dotenv(find_dotenv())

env.root_dir = abspath(join(dirname(realpath(__file__)), pardir))
env.flask_app = join(env.root_dir, 'autoapp.py')
env.build_dir = join(env.root_dir, 'build')
env.gif_dir = join(env.root_dir, 'gifs')

env.remote = ('myles@bear.mylesbraithwaite.com:'
              '/srv/www/mylesb.ca/gifs/html/')

env.giphy_api_key = environ.get('GIPHY_API_KEY', None)
