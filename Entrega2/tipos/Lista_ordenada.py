'''
Created on 10 nov 2024

@author: silva
'''

from __future__ import annotations
from typing import TypeVar

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada:
    def __init__(self, order: Callable[[E], R]) -> None:
        super().__init__()
        self._order = order 

    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        return bisect_left(self._elements, e, key=self._order)

    def add(self, e: E) -> None:
        index = self.__index_order(e)  
        self._elements.insert(index, e)  
        
    def __repr__(self) -> str:
        return (f"ListaOrdenada({', '.join(map(str, self._elements))})")
    

