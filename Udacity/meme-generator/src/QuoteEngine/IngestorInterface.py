"""Define la interfaz para los ingestors de ficheros de citas."""

from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interfaz para los ingestors de ficheros de citas."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Localiza la extensión del fichero y comprueba si es soportada.

           Cada ingestor debe definir su propia lista de
           extensiones soportadas.

        Args:
            path (str): Ruta del fichero a parsear.
            returns (List[QuoteModel]): Lista de QuoteModel del fichero.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parsea un fichero del tipo que se ingesta .

        Args:
            path (str): Ruta del fichero a parsear.
            returns (List[QuoteModel]): Lista de QuoteModel del fichero.
        """
        pass
