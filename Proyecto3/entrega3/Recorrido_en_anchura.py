'''
Created on 14 dic 2024

@author: silva
'''
from __future__ import annotations
from typing import TypeVar
from entrega3.Grafo import Grafo
from entrega3.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')

class Recorrido_en_anchura(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_anchura[V,E]:
        return Recorrido_en_anchura(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
    
    def traverse(self,source:V)->None:
        from collections import deque
        queue = deque([source])
        self._tree[source] = (None, 0)
        while queue:
            v = queue.popleft()
            self._path.append(v)
            for neighbor in self._grafo.successors(v):
                if neighbor not in self._tree:
                    queue.append(neighbor)
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)

if __name__ == '__main__':
    pass