from glob import glob
from os.path import join

from flask import current_app


def all_gifs():
    gifs = []
    gif_files = glob(join(current_app.config['GIFS_PATH'], '**/*.gif'),
                     recursive=True)

    for filename in gif_files:
        gif = current_app.config['GIF_REGEX'].search(filename)
        gifs.append(gif.groups()[0])

    return gifs
