'''
Created on 19 dic 2024

@author: silva
'''
from dataclasses import dataclass

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @classmethod
    def of(cls, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones no puede ser negativo")
        return cls(nombre, tipo, num_mutaciones, loc_cromosoma)

    @classmethod
    def parse(cls, linea: str):
        partes = linea.strip().split(",")
        if len(partes) != 4:
            raise ValueError("Formato incorrecto en la línea")
        return cls.of(partes[0], partes[1], int(partes[2]), partes[3])

    def __str__(self):
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"

# Comprobación del método parse
if __name__ == "__main__":
    prueba_linea = "TP53,supresor tumoral,256,17p13.1"
    gen = Gen.parse(prueba_linea)
    print(gen)
