'''
Created on 10 nov 2024

@author: silva
'''
from typing import Callable, List, TypeVar, Generic
from bisect import bisect_left

E = TypeVar('E') 
R = TypeVar('R') 

class Lista_ordenada_sin_repeticion(Generic[E, R]):
    def __init__(self, order: Callable[[E], R]) -> None:
        super().__init__()
        self._order = order  

    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        return bisect_left(self._elements, e, key=self._order)

    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self.__index_order(e)  
            self._elements.insert(index, e) 

    def __repr__(self) -> str:
        return (f"ListaOrdenadaSinRepeticion({', '.join(map(str, self._elements))})")
    