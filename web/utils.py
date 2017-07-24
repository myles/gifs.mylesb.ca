from glob import glob
from os.path import exists, getmtime, join

import yaml

from flask import current_app


def load_data(slug):
    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if not exists(yaml_file):
        return {}

    with open(yaml_file) as fobj:
        return yaml.load(fobj.read())


def all_gifs():
    gifs = []

    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)
    gif_files = sorted(gif_files, key=lambda x: getmtime(x), reverse=True)

    for filename in gif_files:
        gif = current_app.config['GIF_REGEX'].search(filename)
        gifs.append(gif.groups()[0])

    return gifs
