'''
Created on 10 nov 2024

@author: daniel silva escalera 
'''
from __future__ import annotations
from typing import TypeVar

E = TypeVar('E')

class Agregado_Lineal:
    def __init__(self):
        self._elements: list[E] = []
        
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self)->bool:
        if len(self._elements)==0:
            return True
        else:
            return False
        
    def elements(self) -> list[E]:
        return self._elements

    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: list[E]) -> None:
        for elem in ls:
            self.add(elem)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> list[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements
