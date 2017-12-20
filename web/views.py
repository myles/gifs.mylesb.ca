# -*- coding: utf-8 -*-
"""Views."""
from flask import (Blueprint, abort, current_app, jsonify, render_template,
                   send_from_directory, url_for)

from .pagination import Paginator
from .utils import all_gifs, load_data

blueprint = Blueprint('views', __name__)


@blueprint.route('/')
@blueprint.route('/p<int:page>.html')
def gif_list(page=1):
    """List all Gifs."""
    gifs = all_gifs()

    paginator = Paginator(gifs, 25)

    page = paginator.get_page(page)

    return render_template('gif-list.html', page=page)


@blueprint.route('/api.json')
def gif_list_json():
    """List all Gifs in a JSON format."""
    gifs = all_gifs()

    return jsonify(gifs)


@blueprint.route('/<path:slug>/')
def gif_detail(slug):
    """Get detail of Gif."""
    if slug == 'favicon.ico':
        abort(404)

    gif = load_data(slug)

    return render_template('gif-detail.html', gif=gif)


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


@blueprint.route('/<path:slug>/image.webp')
def gif_image_webp(slug):
    """Get the WebP."""
    return send_from_directory(current_app.config['GIFS_PATH'],
                               '{}.webp'.format(slug))


@blueprint.route('/<path:slug>/api.json')
def gif_detail_json(slug):
    """Get detail of Gif in JSON."""
    gif = load_data(slug)
    return jsonify(gif)


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
