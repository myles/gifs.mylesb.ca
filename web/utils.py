"""Utitlities."""
from datetime import datetime
from glob import glob
from os.path import exists, getmtime, join

import yaml
from dateutil.parser import parse as du_parse
from flask import current_app, url_for
from PIL import Image


def load_data(slug):
    """Load the data."""
    tpl_url = 'https://gifs.mylesb.ca{}'

    data = {
        'slug': slug,
        'image_url': tpl_url.format(url_for('views.gif_image', slug=slug)),
        'html_url': tpl_url.format(url_for('views.gif_detail', slug=slug)),
        'json_url': tpl_url.format(url_for('views.gif_detail_json',
                                           slug=slug))
    }

    gif_file = join(current_app.config['GIFS_PATH'], '{}.gif'.format(slug))
    mp4_file = join(current_app.config['GIFS_PATH'], '{}.mp4'.format(slug))
    webp_file = join(current_app.config['GIFS_PATH'], '{}.webp'.format(slug))

    # If gif doesn't exist rasie a error.
    if not exists(gif_file):
        raise Exception

    if exists(mp4_file):
        data['mp4'] = True
        data['mp4_url'] = tpl_url.format(url_for('views.gif_image_mp4',
                                                 slug=slug))

    if exists(webp_file):
        data['webp'] = True
        data['webp_url'] = tpl_url.format(url_for('views.gif_image_webp',
                                                  slug=slug))

    image = Image.open(gif_file)
    data['width'], data['height'] = image.size

    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if exists(yaml_file):
        with open(yaml_file) as fobj:
            meta = yaml.safe_load(fobj.read())
    else:
        meta = {}

    if not meta.get('date'):
        meta['date'] = datetime.fromtimestamp(getmtime(gif_file))

    if type(meta.get('date')) != datetime:
        meta['date'] = du_parse(meta['date'])

    meta['sort'] = meta['date'].isoformat()

    data.update(meta)

    return data


def all_gifs():
    """Get all the GIFs."""
    gifs = []

    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)

    for filename in gif_files:
        slug = current_app.config['GIF_REGEX'].search(filename).groups()[0]

        gif = load_data(slug)

        gifs.append(gif)

    gifs = sorted(gifs, key=lambda x: x['sort'], reverse=True)

    return gifs
