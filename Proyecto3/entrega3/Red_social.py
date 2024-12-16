'''
Created on 15 dic 2024

@author: silva
'''
from __future__ import annotations
from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from entrega3.Usuario import Usuario
from entrega3.Relacion import Relacion

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
        
    @staticmethod
    def of() -> Red_social:
        return Red_social(Graph_type.UNDIRECTED, Traverse_type.BACK)
    
    @staticmethod
    def parse(f1:str, f2:str, graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        red_social = Red_social(graph_type, traverse_type)
        try:
            with open(f1, 'r') as file:
                for line in file:
                    usuario = Usuario.parse(line.strip())
                    red_social.add_vertex(usuario)
                    red_social.__usuarios_dni[usuario.dni] = usuario
        except FileNotFoundError:
            print(f"Error: El archivo {f1} no se encontró.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo {f1}: {e}")
            return None
        
        try:
            with open(f2, 'r') as file:
                for line in file:
                    id, dni1, dni2, interacciones, dias_activa = line.strip().split(',')
                    usuario1 = red_social.__usuarios_dni[dni1]
                    usuario2 = red_social.__usuarios_dni[dni2]
                    relacion = Relacion.of(int(interacciones), int(dias_activa))
                    red_social.add_edge(usuario1, usuario2, relacion)
        except FileNotFoundError:
            print(f"Error: El archivo {f2} no se encontró.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo {f2}: {e}")
            return None
        
        return red_social

    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni

if __name__ == '__main__':
    rrss: Red_social = Red_social.parse('../resources/usuarios.txt', '../resources/relaciones.txt')
    if rrss:
        print(rrss)
