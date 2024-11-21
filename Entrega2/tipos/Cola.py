'''
Created on 10 nov 2024

@author: silva
'''
from typing import List, TypeVar, Generic

E = TypeVar('E') 

class Cola:
    def __init__(self) -> None:
        super().__init__()
    @classmethod
    def of(cls) -> 'Cola[E]':
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __repr__(self) -> str:
        return f"Cola({', '.join(map(str, self._elements))})"
