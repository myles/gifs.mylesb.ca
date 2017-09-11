"""Utitlities."""
from glob import glob
from os.path import exists, getmtime, join

import yaml
from flask import current_app
from PIL import Image


def load_data(slug):
    """Load the data."""
    data = {}

    gif_file = join(current_app.config['GIFS_PATH'], '{}.gif'.format(slug))
    mp4_file = join(current_app.config['GIFS_PATH'], '{}.mp4'.format(slug))

    # If gif doesn't exist rasie a error.
    if not exists(gif_file):
        raise Exception

    if exists(mp4_file):
        data['mp4'] = True

    image = Image.open(gif_file)
    data['width'], data['height'] = image.size

    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if not exists(yaml_file):
        return data

    with open(yaml_file) as fobj:
        meta = yaml.load(fobj.read())
        return data.update(meta)


def all_gifs():
    """Get all the GIFs."""
    gifs = []

    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)
    gif_files = sorted(gif_files, key=lambda x: getmtime(x), reverse=True)

    for filename in gif_files:
        gif = current_app.config['GIF_REGEX'].search(filename)
        gifs.append(gif.groups()[0])

    return gifs
