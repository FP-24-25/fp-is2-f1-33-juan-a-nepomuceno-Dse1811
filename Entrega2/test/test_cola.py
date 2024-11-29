'''
Created on 11 nov 2024

@author: silva
'''
# Definición de la clase Cola
from typing import List, TypeVar, Generic

E = TypeVar('E')

class Cola(Generic[E]):
    def __init__(self) -> None:
        self._elements: List[E] = [] 

    @classmethod
    def of(cls) -> 'Cola[E]': 
        return cls()

    def add(self, e: E) -> None:
        """Añade un elemento al final de la cola."""
        self._elements.append(e)

    def __repr__(self) -> str:
        """Representación en forma de cadena de la cola."""
        return f"Cola({', '.join(map(str, self._elements))})"

cola = Cola.of() 

cola.add(45)  
cola.add(26)  
cola.add(32)  

print(cola) 
