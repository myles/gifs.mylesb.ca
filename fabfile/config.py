# -*- coding: utf-8 -*-
"""Get Fabric Configuration."""
from os import pardir
from os.path import abspath, dirname, join, realpath

from fabric.api import env

env.root_dir = abspath(join(dirname(realpath(__file__)), pardir))

env.build_dir = join(env.root_dir, 'build')

env.remote = 'myles@bear.mylesbraithwaite.com:/srv/www/mylesb.ca/gifs/html/'
