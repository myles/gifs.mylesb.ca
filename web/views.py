# -*- coding: utf-8 -*-
"""Views."""
from glob import glob
from os.path import exists, join

import yaml

from flask import (Blueprint, abort, current_app, render_template,
                   send_from_directory)

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
def index():
    gifs = []
    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)

    for filename in gif_files:
        gif = current_app.config['GIF_REGEX'].search(filename)
        gifs.append(gif.groups()[0])

    return render_template('index.html', gifs=gifs)


@blueprint.route('/<path:slug>/')
def gif(slug):
    if slug == 'favicon.ico':
        abort(404)

    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if not exists(yaml_file):
        meta = {}
    else:
        with open(yaml_file) as fobj:
            meta = yaml.load(fobj.read())

    return render_template('gif.html', slug=slug, meta=meta)


@blueprint.route('/<path:slug>/image.gif')
def image_gif(slug):
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.gif'.format(slug))
