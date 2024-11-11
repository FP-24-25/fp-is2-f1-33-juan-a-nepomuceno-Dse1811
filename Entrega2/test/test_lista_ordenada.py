'''
Created on 11 nov 2024

@author: silva
'''
from __future__ import annotations
from typing import TypeVar, Callable, List
from bisect import bisect_left

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada:
    def __init__(self, order: Callable[[E], R]) -> None:
        self._order = order
        self._elements: List[E] = [] 

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        return cls(order)

    def __index_order(self, e: E) -> int:
        return bisect_left([self._order(x) for x in self._elements], self._order(e))

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)  

    def __repr__(self) -> str:
        return f"ListaOrdenada({', '.join(map(str, self._elements))})"

lista = Lista_ordenada.of(lambda x: x)

lista.add(3)
lista.add(1)
lista.add(2)

print(lista)  

lista_str = Lista_ordenada.of(lambda x: len(x))

lista_str.add("holaaaa")
lista_str.add("a")
lista_str.add("mundo")

print(lista_str) 
