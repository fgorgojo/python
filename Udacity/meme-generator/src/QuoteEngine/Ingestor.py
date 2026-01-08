"""Define la clase Ingestor que implementa una interfaz única de INGESTA."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .QuoteExc import FileTypeNotSupportedError


class Ingestor(IngestorInterface):
    """Clase que encapsula todos los ingestors.

    Provee interfaz única para cargar cualquier tipo de fichero soportado.
    """

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parsea un fichero y busca un INGESTOR válido.

        Args:
            path (str): Ruta del fichero a parsear.
            returns (List[QuoteModel]): Lista de QuoteModel  del fichero.
        """
        for ingester in cls.ingestors:
            if ingester.can_ingest(path):
                try:
                    return ingester.parse(path)
                except Exception as e:
                    raise e    

        raise FileTypeNotSupportedError(f'No se encontró un ingestor válido' \
                                        f' para este fichero {path}.')