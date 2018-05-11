# -*- coding: utf-8 -*-
"""Click commands."""
from os import environ

import click

from flask import current_app
from flask.cli import with_appcontext
from flask_frozen import Freezer


@click.command()
@with_appcontext
def freeze():
    """Freeze the website before deploy."""
    freezer = Freezer(current_app)
    freezer.freeze()


@click.command()
@with_appcontext
def update_index():
    """Update the Algolia search index."""
    from algoliasearch import algoliasearch

    from .utils import all_gifs

    client = algoliasearch.Client(
        environ.get('ALGOLIA_APP_ID'),
        environ.get('ALGOLIA_API_KEY')
    )

    index = client.init_index(environ.get('ALGOLIA_INDEX_NAME'))

    gifs = all_gifs()

    for gif in gifs:
        gif['objectID'] = gif['slug']

    index.add_objects(gifs)

    index.set_settings({
        'searchableAttributes': ['title', 'slug', 'caption']
    })
