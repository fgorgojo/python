"""Meme Engine Module."""
from importlib.resources import path
import random
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


class MemeEngine:
    """A Meme Engine class to create memes by adding text to images."""

    def __init__(self, outputdir='./tmp'):
        """Meme engine Constructor."""
        self.outputdir = outputdir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme with an image and a quote."""
        # Open an image
        try:
            img = Image.open(img_path)
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise e

        # Max size for width is 500
        if width > 500:
            width = 500

        # Resize the image with width
        new_size = (width, width)
        maxX = width - len(text)*10
        x = random.randint(0, maxX)
        y = random.randint(0, width - 50)
        resized_img = img.resize(new_size)

        # Add text and author to image
        draw = ImageDraw.Draw(resized_img)
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text((x, y), text, fill="white", font=font)
        draw.text((x+10, y+20), author, fill="black", font=font)

        # Save file in output directory format: file_name-author.jpg
        filename = Path(img_path).stem
        outputfile = f"{self.outputdir}/{filename}-{author}.jpg"
        try:
            resized_img.save(outputfile, format="JPEG")
        except Exception as e:
            raise e

        return outputfile
