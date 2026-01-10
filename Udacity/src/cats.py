"""Animmal classes.

Se puede instalar: pip install pydocstyle.
`pydocstyle cats.py` implica la generación de docstrings para las clases y métodos.
Verificar `python cats.py` para verificar el doctest.
"""

class Cat():
    """Define what it is a Cat."""

    def __init__(self, name:str, age:int):
        """Cat attributes."""
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Make a cat sound.
        
        >>> kitty.speak()
        Spot says, purrrrrr.
        """
        print(f'{self.name} says, purrrrrr.')

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'kitty': Cat('Spot', 3)})        