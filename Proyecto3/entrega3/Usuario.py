'''
Created on 15 dic 2024

@author: silva
'''
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re

@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni:str, nombre:str, apellidos:str, fecha_nacimiento:date) -> Usuario:
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def parse(linea:str) -> Usuario:
        dni, nombre, apellidos, fecha_nacimiento = linea.split(',')
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
        
    def __str__(self):
        return f'{self.dni} - {self.nombre} {self.apellidos}'

if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)