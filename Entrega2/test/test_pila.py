'''
Created on 11 nov 2024

@author: silva
'''
from typing import Generic, List, TypeVar

E = TypeVar('E')

class Agregado_lineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    def is_empty(self) -> bool:
        return len(self._elements) == 0

class Pila(Agregado_lineal[E]):
    @classmethod 
    def of(cls) -> 'Pila[E]':
        return cls()

    def add(self, e: E) -> None:
        """Añade un elemento a la parte superior de la pila."""
        self._elements.insert(0, e)  

    def __repr__(self) -> str:
        return f"Pila({', '.join(map(str, self._elements))})"

pila = Pila.of() 

pila.add(1)  
pila.add(2)  
pila.add(3)  

print(pila) 

print(pila.is_empty())  

pila.add(4)  

print(pila) 
