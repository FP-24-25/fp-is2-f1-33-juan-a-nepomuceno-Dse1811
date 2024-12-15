'''
Created on 15 dic 2024

@author: silva
'''
from __future__ import annotations
from typing import TypeVar, Callable
from enum import Enum
from entrega3.Grafo import Grafo

V = TypeVar('V')
E = TypeVar('E')

class Graph_type(Enum):
    UNDIRECTED = 1
    DIRECTED = 2

class Traverse_type(Enum):
    FORWARD = 1
    BACK = 2

class E_grafo(Grafo[V,E]):
    
    def __init__(self,graph_type:Graph_type,weight:Callable[[E],float],traverse_type:Traverse_type=Traverse_type.FORWARD)->None:
        self._vertex_set:set[V] = set()
        self._edge_set:set[E] = set()
        self._edges_dict:dict[tuple[V,V],E] = {}
        self._neighbors:dict[V,set[V]] = {}
        self._predecessors:dict[V,set[V]] = {}
        self._sources:dict[E,V] = {}
        self._targets:dict[E,V] = {}
        self._graph_type = graph_type
        self._weight = weight
        self._traverse_type = traverse_type
     
    def __add_neighbors(self, source:V, target:V)->None:
        if source not in self._neighbors:
            self._neighbors[source] = set()
        self._neighbors[source].add(target)
            
    def __add_predecessors(self, source:V, target:V)->None:
        if target not in self._predecessors:
            self._predecessors[target] = set()
        self._predecessors[target].add(source)

    def add_edge(self,source:V,target:V,e:E)->None:
        if source in self._vertex_set and target in self._vertex_set and source != target and (source, target) not in self._edges_dict:
            self._edge_set.add(e)
            self._edges_dict[(source, target)] = e
            self._sources[e] = source
            self._targets[e] = target
            self.__add_neighbors(source, target)
            if self._graph_type == Graph_type.DIRECTED:
                self.__add_predecessors(source, target)
            else:
                self.__add_neighbors(target, source)

    def edge_weight(self,sourceVertex:V, targetVertex:V) -> float:
        return self._weight(self._edges_dict[(sourceVertex, targetVertex)])
    
    def add_vertex(self,vertex:V)->bool:
        if vertex not in self._vertex_set:
            self._vertex_set.add(vertex)
            return True
        return False
    
    def edge_source(self,e:E)->V:
        return self._sources[e]
    
    def edge_target(self,e:E)->V:
        return self._targets[e]
    
    def vertex_set(self)->set[V]:
        return self._vertex_set
     
    def edge_set(self)->set[E]:
        return self._edge_set
    
    def contains_edge(self,sourceVertex:V, targetVertex:V)->bool:
        return (sourceVertex, targetVertex) in self._edges_dict
     
    def neighbors(self,vertex:V)->set[V]:
        return self._neighbors.get(vertex,set())
    
    def predecessors(self,vertex:V)->set[V]:
        return self._predecessors.get(vertex,set())
        
    def successors(self,vertex:V)->set[V]:
        if self._traverse_type == Traverse_type.FORWARD:
            return self.neighbors(vertex)
        else:
            return self.predecessors(vertex)
    
    def edge(self,sourceVertex:V, targetVertex:V) -> E:
        return self._edges_dict[(sourceVertex,targetVertex)]
            
    def vertex_list(self)->list[V]:
        return list(self._vertex_set)
    
    def graph_type(self)->Graph_type:
        return self._graph_type
    
    def traverse_type(self)->Traverse_type:
        return self._traverse_type
    
    def weight(self)->Callable[[E],float]:
        return self._weight
    
    def inverse_graph(self)->E_grafo[V,E]:
        if self._graph_type == Graph_type.UNDIRECTED:
            return self
        g:E_grafo[V,E] = E_grafo(self.graph_type(),self.weight(),self.traverse_type())
        for v in self._vertex_set:
            g.add_vertex(v)
        for e in self._edge_set:
            s = self.edge_source(e)
            t = self.edge_target(e)
            g.add_edge(t, s, e)
        return g
    
    def subgraph(self,vertices:set[V]) -> Grafo[V,E]:
        g:E_grafo[V,E] = E_grafo(self.graph_type(),self.weight(),self.traverse_type())
        for v in vertices:
            g.add_vertex(v)
        for e in self.edge_set():
            s = self.edge_source(e)
            t = self.edge_target(e)
            if s in vertices and t in vertices:
                g.add_edge(s,t,e)
        return g
            
    def __str__(self):
        sep = '\n'
        return f'Vertices: \n{sep.join(str(x) for x in self._vertex_set)} \nAristas: \n{sep.join(str(x) for x in self._edge_set)}'

if __name__ == '__main__':
    pass