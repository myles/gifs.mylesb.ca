from glob import glob
from os.path import exists, join

import yaml

from flask import current_app


def all_gifs():
    gifs = []
    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)

    for filename in gif_files:
        gif = current_app.config['GIF_REGEX'].search(filename)
        gifs.append(gif.groups()[0])

    return gifs


def load_data(slug):
    yaml_file = join(current_app.config['GIFS_PATH'], '{}.yml'.format(slug))

    if not exists(yaml_file):
        return {}

    with open(yaml_file) as fobj:
        return yaml.load(fobj.read())
