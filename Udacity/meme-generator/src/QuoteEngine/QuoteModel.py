"""Encapsula una cita con su cuerpo y autor."""


class QuoteModel:
    """Clase que encapsula una cita con su cuerpo y autor."""

    def __init__(self, body: str, author: str):
        """Construye un QuoteModel."""
        self.body = body
        self.author = author

    def __str__(self):
        """Visualiza un QuoteModel."""
        return f'{self.body} - {self.author}'
