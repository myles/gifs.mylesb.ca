# -*- coding: utf-8 -*-
"""Views."""
from flask import (Blueprint, abort, current_app, jsonify, render_template,
                   send_from_directory, url_for)
from web.utils import all_gifs, load_data

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
def gif_list():
    gifs = all_gifs()

    return render_template('gif-list.html', gifs=gifs)


@blueprint.route('/api.json')
def gif_list_json():
    tpl_url = 'https://mylesb.ca{}'
    gifs = all_gifs()

    resp = []
    for slug in gifs:
        resp.append({
            'slug': slug,
            'meta': load_data(slug),
            'image_url': tpl_url.format(url_for('views.gif_image', slug=slug)),
            'html_url': tpl_url.format(url_for('views.gif_detail', slug=slug))
        })

    return jsonify(resp)


@blueprint.route('/<path:slug>/')
def gif_detail(slug):
    if slug == 'favicon.ico':
        abort(404)

    meta = load_data(slug)

    return render_template('gif-detail.html', slug=slug, meta=meta)


@blueprint.route('/<path:slug>/image.gif')
def gif_image(slug):
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.gif'.format(slug))


@blueprint.route('/<path:slug>/api.json')
def gif_detail_json(slug):
    resp = {
        'slug': slug,
        'meta': load_data(slug),
        'image_url': url_for('views.gif_image', slug=slug),
        'html_url': url_for('views.gif_detail', slug=slug)
    }

    return jsonify(resp)
