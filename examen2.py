'''
Created on 21 nov 2024

@author: silva
'''
#-------------------------EJERCICIO 1-----------------------------------------------
from typing import List, TypeVar, Generic

class ColaConLimite:
    def __init__(self, capacidad):
        if capacidad<=0:
            raise ValueError('Obligatorio: capacidad>0')
        else:
            self.capacidad=capacidad
            self.cola=[]
    
    def is_full(self):
        return len(self.cola) >= self.capacidad
    
    def add(self, elemento):
        if self.is_full():
            raise OverflowError("La cola está llena.")
        else:
            self.cola.append(elemento)
    
    def remove(self):
        if not self.cola:
            raise IndexError("La cola está vacía.")
        else:
            return self.cola.pop(0)
    
    @classmethod
    def of(cls, capacidad):
        return cls(capacidad)

#-----------------------------------------------------------------------------------
#------------------------EJERCICIO 2------------------------------------------------
from typing import Callable, TypeVar, Generic, List

E = TypeVar('E')  # Define un tipo genérico

class AgregadoLineal(Generic[E]):
    def __init__(self):
        self.elementos: List[E] = []

    def add(self, elemento: E):
        self.elementos.append(elemento)

    def remove(self) -> E:
        if not self.elementos:
            raise IndexError("El agregado está vacío.")
        return self.elementos.pop(0)

    def contains(self, e: E) -> bool:
        return e in self.elementos

    def find(self, func: Callable[[E], bool]) -> E | None:
        for elemento in self.elementos:
            if func(elemento):
                return elemento
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [elemento for elemento in self.elementos if func(elemento)]
#-----------------------------------------------------------------------------------
#------------------------EJERCICIO 3------------------------------------------------
print('TEST EJERCICIO 1')#EN LA PROPIA HOJA DEL EXAMEN APARECEN LOS RESULTADO QUE DEBEN APARECER
cola=ColaConLimite.of(3)
cola.add('Tarea 1')
cola.add('Tarea 2')
cola.add('Tarea 3')
try:
    cola.add('Tarea 4')
except OverflowError as e:
    print(e)
print(cola.remove())
print('')
print('TEST EJERCICIO 2')#VOY A DETALLAR QUE RESULTADOS DEBERÍAN DE SALIR EN LAS COMPROBACIONES
agregado = AgregadoLineal[int]()
agregado.add(1)
agregado.add(2)
agregado.add(3)
agregado.add(4)

# Verificar si contiene un elemento
print(agregado.contains(2))  # Debe salir True
print(agregado.contains(5))  # Debe salir False

# Encontrar el primer elemento mayor que 2
print(agregado.find(lambda x: x > 2))  # Debe salir 3

# Filtrar elementos pares
print(agregado.filter(lambda x: x % 2 == 0))  #Debe salir [2, 4]