"""Ingestor para ficheros de tipo .pdf."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Clase para ingestar ficheros pdf."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parsea un fichero pdf y devuelve una lista de QuoteModel.

        Args:
            path (str): Ruta del fichero a parsear.
            returns (List[QuoteModel]): Lista de QuoteModel
            parseados del fichero.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp], shell=True)

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
