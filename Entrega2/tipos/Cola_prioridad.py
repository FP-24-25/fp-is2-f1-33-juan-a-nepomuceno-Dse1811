'''
Created on 10 nov 2024

@author: silva
'''

'''NO CORREGIR'''

from typing import List, TypeVar, Tuple, Callable

E = TypeVar('E')  
P = TypeVar('P')  

class ColaPrioridad:
    def __init__(self) -> None:
        self._elements: List[E] = [] 
        self._priorities: List[P] = [] 

    def of(cls) -> 'ColaPrioridad[E, P]':
        return cls()

    def add(self, e: E, priority: P) -> None:
        index = self.index_order(priority)  
        self._elements.insert(index, e) 
        self._priorities.insert(index, priority) 

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'  
        self._priorities.pop(0)  
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = self._elements.copy() 
        self._elements.clear() 
        self._priorities.clear() 
        return removed_elements 

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def size(self) -> int:
        return len(self._elements)

    def elements(self) -> List[E]:
        return self._elements

    def index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if p < priority:  
                return i
        return len(self._elements)

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            old_priority = self._priorities[index]
            if new_priority < old_priority: 
                self._priorities.pop(index)
                self._elements.pop(index)
                self.add(e, new_priority)  

    def __repr__(self) -> str:
        return f"ColaPrioridad[{', '.join(f'({e}, {p})' for e, p in zip(self._elements, self._priorities))}]"
