class QuoteException(Exception):
    """Excepción personalizada para errores relacionados con citas."""
    pass    

class FileTypeNotSupportedError(QuoteException):
    """Excepción para tipos de archivo no soportados."""

    def __init__(self, message="El tipo de archivo no es soportado."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'FileTypeNotSupportedError: {self.message}'
    
class  FileNotFoundError(QuoteException):
    """Excepción para cuando no se encuentra el fichero."""

    def __init__(self, message="Fichero no encontrado."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'FileNotFoundError: {self.message}'
    
class QuoteParseError(QuoteException):
    """Excepción para errores durante el parseo de citas."""

    def __init__(self, message="Error al parsear la cita."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'QuoteParseError: {self.message}'

class EmptyQuoteError(QuoteException):
    """Excepción para citas vacías."""

    def __init__(self, message="La cita está vacía."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'EmptyQuoteError: {self.message}'
    
class AuthorNotFoundError(QuoteException):
    """Excepción para cuando no se encuentra el autor de una cita."""

    def __init__(self, message="Autor de la cita no encontrado."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'AuthorNotFoundError: {self.message}'
