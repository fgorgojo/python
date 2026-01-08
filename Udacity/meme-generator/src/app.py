"""Meme`s web generator server."""

import random
import os
import requests
import tempfile
from flask import Flask, render_template, abort, request
from urllib.parse import urlparse

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine.Ingestor import Ingestor, QuoteModel
from MemeEngine.memeGenerator import MemeEngine
from typing import List

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for pathfile in quote_files:
        lista = []
        lista = Ingestor.parse(pathfile)
        quotes = quotes + lista

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    img = random.choice(imgs)
    # 2. select a random quote from the quotes array
    quote = random.choice(quotes)

    # quote = QuoteModel('Vive y deja vivir','Paul Macartney')
    path = meme.make_meme(img, quote.body, quote.author)
    print("Rendereing .....")
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    body = request.form.get('body')
    author = request.form.get('author')
    image_url = request.form.get('image_url')

    # 2. Use the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    temp_path = urlparse(image_url).path[1:]
    path = meme.make_meme(temp_path, body, author)

    # 3. Remove the temporary saved image.
    # os.remove(temp_path)

    return render_template('meme.html', path=path)
