"""—————————————————————
    Clase Algoritmo.
—————————————————————"""
from copy import copy  # Acciones de copiado en arreglos.
from collections import deque  # Acciones de tratado de colas y pilas.


class Algoritmo:

    """——————————————————————00——————————————————————CONSTRUCTOR—————————————————————————————————————————————————————"""
    def __init__(self, nombre, grafo):
        self.nombre = nombre
        self.grafo = grafo

    """══════════════════════════════════════════════ALGORITMOS══════════════════════════════════════════════════════"""

    """——————————————————————01——————————————————————PRIM————————————————————————————————————————————————————————————"""
    def prim(self):
        # print('Ingreso prim')
        aristas_copia = copy(self.grafo.get_lista_aristas())  # Aristas originales.
        aristas_temp = []  # Listado amarillo de aristas.
        conjunto = []  # Listado de vértices a dar verificaciones.
        aristas_arbol = []  # Conjunto de aristas que cumplen con el criterio del alg. de Prim.

        # Volvamos dirigido el grafo.
        self.grafo.hacer_dirigido(aristas_copia)

        # Ordenamos el grafo.
        self.grafo.ordenar(aristas_copia)
        menor = aristas_copia[0]

        conjunto.append(menor.get_origen())

        repeat = True
        while repeat:
            # Inicialización del algoritmo de Prim.
            self.algoritmo_prim(aristas_copia, aristas_temp, aristas_arbol, conjunto)
            if len(conjunto) == len(self.grafo.get_lista_vertices()):
                # Se hace retorno de la lista cuando esté completa.
                return conjunto, aristas_arbol
                # repeat = False    # COMENTADO DE CICLO (NO MÁS IMPRESIONES)

            # Impresiones.

            # print(conjunto) # COMENTADO DE IMPRESIONES
            # for arista in aristas_arbol:
                # print('[ Arista: ', arista.get_origen(), '→', arista.get_destino(), ' | Peso: ', arista.get_peso(), ']')

    def algoritmo_prim(self, aristas_copia, aristas_temp, aristas_arbol, conjunto):
        ciclo = False

        # Adición de vértices adyacentes al árbol.
        for vertice in conjunto:
            self.add_temp(aristas_copia, aristas_temp, vertice)

        # Búsqueda de candidata entre aristas amarillas.
        candidata = self.candidata_prim(aristas_temp)

        if candidata and candidata.get_paso():
            # Evitar ciclos.
            if candidata.get_origen() in conjunto and candidata.get_destino() in conjunto:
                ciclo = True
            # Adición de aristas mínimas.
            if not ciclo:
                aristas_arbol.append(candidata)
                # Adición de vértices respectivos.
                if not candidata.get_origen() in conjunto:
                    conjunto.append(candidata.get_origen())
                if not candidata.get_destino() in conjunto:
                    conjunto.append(candidata.get_destino())

    @staticmethod
    def add_temp(aristas_copia, aristas_temp, vertice):
        # Generador de la lista de aristas potenciales (amarillas).
        for arista in aristas_copia:
            # obtención de arista adyacente al vértice (X).
            if arista.get_origen() == vertice or arista.get_destino() == vertice:
                aristas_temp.append(arista)
                aristas_copia.pop(aristas_copia.index(arista))

    @staticmethod
    def candidata_prim(aristas_temp):
        if len(aristas_temp) > 0:
            min = aristas_temp[len(aristas_temp) - 1]
            for arista in aristas_temp:
                if arista.get_peso() < min.get_peso():
                    min = arista
            aristas_temp.pop(aristas_temp.index(min))
            return min
        # Lista sin elementos:
        return None

    """——————————————————————02——————————————————————DIJKSTRA————————————————————————————————————————————————————————"""
    def dijkstra(self):
        print('Algoritmo de Dijkstra.')
        return ['Algoritmo', 'Dijkstra']

    """——————————————————————03——————————————————————KRUSKAL—————————————————————————————————————————————————————————"""
    def kruskal(self):
        print('Algoritmo de Kruskal.')
        return ['Algoritmo', 'Kruskal']

    """——————————————————————04——————————————————————BORUVKA—————————————————————————————————————————————————————————"""
    def boruvka(self):
        print('Algoritmo de Boruvka.')
        return ['Algoritmo', 'Boruvka']

    """══════════════════════════════════════════════RECORRIDOS══════════════════════════════════════════════════════"""

    """——————————————————————04——————————————————————ANCHURA—————————————————————————————————————————————————————————"""
    def anchura(self):
        # print('Recorrido de anchura.')
        return ['Recorrido', 'anchura']

    """——————————————————————04——————————————————————PROFUNDIDAD—————————————————————————————————————————————————————"""
    def profundidad(self):
        print('Recorrido profundidad.')
        return ['Recorrido', 'profundidad']

    """——————————————————————04——————————————————————FLOYD—WARSHALL——————————————————————————————————————————————————"""
    def floyd_warshall(self):
        print('Recorrido de Floyd Warshall.')
        return ['Floyd', 'Warshall']

    """——————————————————————04——————————————————————FORD—FULKERSON——————————————————————————————————————————————————"""
    def ford_fulkerson(self):
        print('Recorrido de Ford Fulkerson.')
        return ['Ford', 'Fulkerson']
