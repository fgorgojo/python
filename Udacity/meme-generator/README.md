# Meme generator
Expose an URL endpoint for the user to generate memes. 
The memes are composed by images and within quotes ( description and author name )

There are two URL presented in template folder:
 - For random generated images: `meme.html`: 
   It displays random images with embedded quotes at different points in the image. 
 - For custom generated images posting input data within a given form: `meme_form.html`
   It shows a form to input URL with base image, body and names quotes to be displayes.

## CLI Execution .
- Execution of MemeEngine from cli.
  From proyect base path meme-generator:
  python meme.py
  paremeters: ( All are optionals.)
    - path: source path to cature images. Default (.\src\_data\photos\)
    - body: quote description. Default ( row description sample from .\src\_data\DogQuotes)
    - author: quote author name  ( row name sample from .\src\_data\DogQuotes)
  
- Example:
  ```
  cd src
  python .\meme.py --body "No hay mal que por bien no venga" --author "Fernando Gorgojo"
  ```
  
## WEB SERVER Execution:
 - Using Flask third party library:
   Use these instructions to set up the flask server
    ```
    cd src
    export FLASK_APP=app.py
    flask run --host 0.0.0.0 --port 3000 --reload
    ```
 - Open URL https://localhost:3000/  : 
    This endpoint render `meme.html`
 - Open URL https://localhost:3000/create  : 
    This endpoint render `meme_form.html` for POST method.
    This endpoint render `meme.html` for GET method to recover the generated image with the form parameters.


## Proyect Structure

meme-generator
    src
        _data                    -- Data with quotes and images downloaded 
        MemeEngine               -- Package meme generator
            __init.py
            memeGenerator        -- Meme generator module
        QuoteEngine              -- Package quote engine
            __init.p
            CVSIngestor.py       -- CSV specialized ingestor
            DocxIngestor.py      -- Docx specialized ingestor
            PDFIngestor.py       -- PDF specialized ingestor
            TXTIngestor.py       -- TXT specialized ingestor
            QuoteExc.py          -- App user defined exceptionis
            QuotMode.py          -- Support for quotes: body and name
            Ingestor.py          -- Ingestor general abstraction
            IngestorInterface.py -- Ingestor interface
        templates                -- Browser templates
        static                   -- Default output generation path 
        tmp                      -- Temporal files
        app.py                   -- Flask server
        meme.py                  -- meme generator
    README.md                    -- This doc
    requirements.txt             -- External dependencies
    memenv                       -- Dedicated virtual environment 
    
### Modules and packages description
 - app.py - Sets up a image and quotes rendering FLASK server.
 - meme.py  - Image generator 
 - QuoteEngine - Edit images and writes author and body quotes on images randomly
 - MemeEngine - Ingest authors and body data from different sources. 
 
## Virtual environment and dependdencies:
It is provided a file requirements for external libraries. 
 `memenv` folder it is the virtual enviroment for this project
 
 - Virtual environment creation: deactivate another one and activate again:
```
deactivate
.\memenv\Scripts\Activate.ps1
```
  Check from powershell you are using the right virtual environment:
  `Get-Command python` or `where python`

 - For creation all external dependencies: 
    `python -m pip install --upgrade pip`
    `pip install -r .\requirements.txt`

## PEP-8 compliant utilities
 - Apply in every module both `pydocstyle` and `pycodestyle` tools.

