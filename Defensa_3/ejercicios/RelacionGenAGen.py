'''
Created on 19 dic 2024

@author: silva
'''
from dataclasses import dataclass

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @classmethod
    def of(cls, nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe estar entre -1 y 1")
        return cls(nombre_gen1, nombre_gen2, conexion)

    @classmethod
    def parse(cls, linea: str):
        partes = linea.strip().split(",")
        if len(partes) != 3:
            raise ValueError("Formato incorrecto en la línea")
        return cls.of(partes[0], partes[1], float(partes[2]))

    @property
    def coexpresados(self):
        return self.conexion > 0.75

    @property
    def antiexpresados(self):
        return self.conexion < -0.75

    def __str__(self):
        return f"RelacionGenAGen(nombre_gen1='{self.nombre_gen1}', nombre_gen2='{self.nombre_gen2}', conexion={self.conexion})"

# Comprobación del método parse
if __name__ == "__main__":
    prueba_linea = "TP53,EGFR,0.5"
    relacion = RelacionGenAGen.parse(prueba_linea)
    print(relacion)
    print("¿Coexpresados?:", relacion.coexpresados)
    print("¿Antiexpresados?:", relacion.antiexpresados)
