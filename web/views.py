# -*- coding: utf-8 -*-
"""Views."""
from os.path import exists, join

import yaml

from flask import (Blueprint, abort, current_app, render_template,
                   send_from_directory)
from web.utils import all_gifs

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
def gif_list():
    gifs = all_gifs()

    return render_template('gif-list.html', gifs=gifs)


@blueprint.route('/<path:slug>/')
def gif_detail(slug):
    if slug == 'favicon.ico':
        abort(404)

    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if not exists(yaml_file):
        meta = {}
    else:
        with open(yaml_file) as fobj:
            meta = yaml.load(fobj.read())

    return render_template('gif-detail.html', slug=slug, meta=meta)


@blueprint.route('/<path:slug>/image.gif')
def image_gif(slug):
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.gif'.format(slug))
