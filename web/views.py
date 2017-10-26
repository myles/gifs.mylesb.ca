# -*- coding: utf-8 -*-
"""Views."""
from flask import (Blueprint, abort, current_app, jsonify, render_template,
                   send_from_directory, url_for)
from pypages import Paginator

from .utils import all_gifs, load_data

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
@blueprint.route('/p<int:page>.html')
def gif_list(page=1):
    """List all Gifs."""
    per_page = 12

    gifs = all_gifs()

    pages = Paginator(len(gifs), per_page=per_page, current=page)

    if page > 1:
        start = (page - 1) * per_page - 1
    else:
        start = 0

    end = page * per_page - 1

    return render_template('gif-list.html', gifs=gifs[start:end], pages=pages)


@blueprint.route('/api.json')
def gif_list_json():
    """List all Gifs in a JSON format."""
    tpl_url = 'https://gifs.mylesb.ca{}'
    gifs = all_gifs()

    resp = []

    for slug in gifs:
        resp.append({
            'slug': slug,
            'meta': load_data(slug),
            'image_url': tpl_url.format(url_for('views.gif_image', slug=slug)),
            'mp4_url': tpl_url.format(url_for('views.gif_image_mp4',
                                              slug=slug)),
            'html_url': tpl_url.format(url_for('views.gif_detail', slug=slug)),
            'json_url': tpl_url.format(url_for('views.gif_detail_json',
                                               slug=slug))
        })

    return jsonify(resp)


@blueprint.route('/<path:slug>/')
def gif_detail(slug):
    """Get detail of Gif."""
    if slug == 'favicon.ico':
        abort(404)

    meta = load_data(slug)

    return render_template('gif-detail.html', slug=slug, meta=meta)


@blueprint.route('/<path:slug>/image.gif')
def gif_image(slug):
    """Get the Gif."""
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.gif'.format(slug))


@blueprint.route('/<path:slug>/image.mp4')
def gif_image_mp4(slug):
    """Get the MP4."""
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.mp4'.format(slug))


@blueprint.route('/<path:slug>/api.json')
def gif_detail_json(slug):
    """Get detail of Gif in JSON."""
    tpl_url = 'https://gifs.mylesb.ca{}'

    resp = load_data(slug)

    resp['slug'] = slug
    resp['image_url'] = tpl_url.format(url_for('views.gif_image', slug=slug))
    resp['html_url'] = tpl_url.format(url_for('views.gif_detail', slug=slug))

    if resp.get('mp4'):
        resp['mp4_url'] = tpl_url.format(url_for('views.gif_image_mp4',
                                                 slug=slug))

    return jsonify(resp)


@blueprint.route('/<path:slug>/oembed.json')
def gif_oembed_json(slug):
    """Get the Gif in oEmbed format."""
    tpl_url = 'https://gifs.mylesb.ca{}'

    data = load_data(slug)

    resp = {
        'version': '1.0',
        'type': 'photo',
        'url': tpl_url.format(url_for('views.gif_image', slug=slug)),
        'provider_name': "Myles' Gifs",
        'provider_url': 'https://gifs.mylesb.ca/',
    }

    if data:
        resp['width'] = data['width']
        resp['height'] = data['height']

    return jsonify(resp)
