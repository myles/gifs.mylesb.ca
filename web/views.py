# -*- coding: utf-8 -*-
"""Views."""
from feedgen.feed import FeedGenerator
from flask import (Blueprint, abort, current_app, jsonify, make_response,
                   render_template, send_from_directory, url_for)

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


@blueprint.route('/feed.json')
@blueprint.route('/feed-<int:page>.json')
def gif_list_jsonfeed(page=1):
    """Generate an ATOM Feed."""
    gifs = all_gifs()

    paginator = Paginator(gifs, 25)

    page = paginator.get_page(page)

    feed = {
        'title': "Myles' GIFs",
        'home_page_url': 'https://gifs.mylesb.ca/',
        'feed_url': 'https://gifs.mylesb.ca{}'.format(
            url_for('views.gif_list_jsonfeed')),
        'items': []
    }

    if page.has_next:
        feed['next_url'] = 'https://gifs.mylesb.ca{}'.format(
            url_for('views.gif_list_jsonfeed', page=page.next_page_number))

    for gif in page.object_list:
        feed_entry = {}
        feed_entry['id'] = gif['html_url']
        feed_entry['url'] = gif['html_url']
        feed_entry['title'] = gif.get('caption', 'GIF')
        feed_entry['content_html'] = (
            '<a href="{html_url}"><img src="{image_url}"></a>').format(**gif)
        feed_entry['author'] = {'name': 'Myles', 'url': 'https://mylesb.ca'}
        feed_entry['image'] = gif['image_url']
        feed_entry['date_published'] = gif['date']

        feed['items'] += [feed_entry]

    return jsonify(feed)


@blueprint.route('/atom.xml')
def gif_list_atom():
    """Generate an ATOM Feed."""
    gifs = all_gifs()[:10]

    feed_gen = FeedGenerator()
    feed_gen.id('https://gifs.mylesb.ca/')
    feed_gen.title("Myles' GIFs")
    feed_gen.link(
        href='https://gifs.mylesb.ca/{}'.format(
            url_for('views.gif_list_atom')),
        rel='self')

    for gif in gifs:
        feed_entry = feed_gen.add_entry()
        feed_entry.id(gif['html_url'])
        feed_entry.title(gif.get('caption', 'GIF'))
        feed_entry.description(('<a href="{html_url}">'
                                '<img src="{image_url}"></a>').format(**gif))
        feed_entry.author({'name': 'Myles', 'email': 'me@mylesb.ca'})
        feed_entry.enclosure(gif['image_url'])

    response = make_response(feed_gen.atom_str(pretty=True))
    response.headers['Content-Type'] = 'application/xml'

    return response


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
        'provider_name': "Myles' GIFs",
        'provider_url': 'https://gifs.mylesb.ca/',
    }

    if data:
        resp['width'] = data['width']
        resp['height'] = data['height']

    return jsonify(resp)
