'''
Created on 14 dic 2024

@author: silva
'''
from __future__ import annotations
from typing import TypeVar
from entrega3.Recorrido import Recorrido
from entrega3.Grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class Recorrido_en_profundidad(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_profundidad[V,E]:
        return Recorrido_en_profundidad(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
    
    def traverse(self,source:V)->None:
        stack = [source]
        self._tree[source] = (None, 0)
        while stack:
            v = stack.pop()
            self._path.append(v)
            for neighbor in self._grafo.successors(v):
                if neighbor not in self._tree:
                    stack.append(neighbor)
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)

if __name__ == '__main__':
    pass