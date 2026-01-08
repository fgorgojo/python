"""Ingestor para ficheros de tipo CSV."""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Clase para ingestar ficheros CSV."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parsea un fichero CSV y devuelve una lista de QuoteModel.

        Args:
            path (str): Ruta del fichero a parsear.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
