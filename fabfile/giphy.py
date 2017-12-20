import datetime
import os.path
import shutil

import requests

from fabric.api import env, task
from fabric.utils import error


def download_image(url, slug):
    extension = os.path.splitext(url)[1]

    resp = requests.get(url, stream=True)

    if not resp.ok:
        error('There was a problem downloading the image.')

    filepath = os.path.join(env.gif_dir, '{0}{1}'.format(slug, extension))

    if os.path.isfile(filepath):
        error('File with that slug already exists.')

    with open(filepath, 'wb') as fobj:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, fobj)


@task
def download(gif_id, slug=None):
    params = {'api_key': env.giphy_api_key}
    url = 'http://api.giphy.com/v1/gifs/{}'.format(gif_id)
    resp = requests.get(url, params=params)

    if not resp.status_code == 200:
        error('GIPHY responded with {}'.format(resp.status_code))

    gif = resp.json()

    if not gif['meta']['status'] == 200:
        error('GIPHY responded with: {}'.format(gif['meta']['msg']))

    if not slug:
        slug = gif['data']['slug']

    image = gif['data']['images']['original']

    download_image(image['url'], slug)

    if image.get('mp4'):
        download_image(image['mp4'], slug)

    if image.get('webp'):
        download_image(image['webp'], slug)

    with open(os.path.join(env.gif_dir, '{}.yml'.format(slug)), 'w') as fobj:
        if gif['data'].get('title'):
            fobj.write('title: "{title}"\n'.format(**gif['data']))

        if gif['data'].get('source'):
            fobj.write('source: "{source}"\n'.format(**gif['data']))
        elif gif['data'].get('url'):
            fobj.write('source: "{url}"\n'.format(**gif['data']))

        date = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')

        fobj.write('date: {}\n'.format(date))
