'''
Created on 19 dic 2024

@author: silva
'''
from ejercicios.Gen import Gen
from ejercicios.RelacionGenAGen import RelacionGenAGen

class E_grafo:
    def __init__(self, weight):
        self.vertices = set()
        self.aristas = []
        self.weight = weight

    def add_edge(self, v1, v2, relacion):
        self.vertices.add(v1)
        self.vertices.add(v2)
        self.aristas.append(relacion)

class RedGenica(E_grafo):
    def __init__(self, genes_por_nombre: dict):
        super().__init__(weight=lambda relacion: relacion.conexion)
        self.genes_por_nombre = genes_por_nombre

    @classmethod
    def parse(cls, path_genes: str, path_relaciones: str):
        genes_por_nombre = {}
        with open(path_genes, 'r') as f:
            for linea in f:
                gen = Gen.parse(linea)
                genes_por_nombre[gen.nombre] = gen

        red = cls(genes_por_nombre)

        with open(path_relaciones, 'r') as f:
            for linea in f:
                relacion = RelacionGenAGen.parse(linea)
                red.add_edge(genes_por_nombre[relacion.nombre_gen1],
                             genes_por_nombre[relacion.nombre_gen2],
                             relacion)
        return red

    def __str__(self):
        vertices = "\n".join(str(gen) for gen in self.genes_por_nombre.values())
        aristas = "\n".join(str(arista) for arista in self.aristas)
        return f"Vertices:\n{vertices}\n\nAristas:\n{aristas}"

# Comprobación del método parse
if __name__ == "__main__":
    ruta_genes = "../data/genes.txt"
    ruta_relaciones = "../data/red_genes.txt"

    red_genica = RedGenica.parse(ruta_genes, ruta_relaciones)
    print(red_genica)
