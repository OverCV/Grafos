"""—————————————————
    Clase Grafo.
—————————————————"""

from modelos.vertice import Vertice
from modelos.arista import Arista
from modelos.algoritmo import Algoritmo


class Grafo:

    """——————————————————————00——————————————————————CONSTRUCTOR—————————————————————————————————————————————————————"""
    def __init__(self):
        self.lista_vertices = []
        self.lista_aristas = []

    def get_lista_vertices(self):
        return self.lista_vertices

    def set_lista_vertices(self, lista):
        self.lista_vertices = lista

    def get_lista_aristas(self):
        return self.lista_aristas

    def set_lista_aristas(self, lista):
        self.lista_aristas = lista

    """——————————————————————01——————————————————————VÉRTICES————————————————————————————————————————————————————————"""

    def ingresar_vertice(self, dato):
        if not self.existe_vertice(dato, self.lista_vertices):
            self.lista_vertices.append(Vertice(dato))

    def mostrar_vertices(self) -> bool:
        s = '['
        for i in range(len(self.lista_vertices)):
            if i < (len(self.lista_vertices) - 1):
                s += " '" + self.lista_vertices[i].get_dato() + "' -"
            else:
                s += " '" + self.lista_vertices[i].get_dato() + "' ]"
        if s == '[':
            print('[ — ]')
            return False
        print(s)
        return True

    @staticmethod
    def obtener_vertice(origen, lista_vertices):
        for i in range(len(lista_vertices)):
            if origen == lista_vertices[i].get_dato():
                return lista_vertices[i]

    @staticmethod
    def existe_vertice(dato, lista_vertices):
        for i in range(len(lista_vertices)):
            if dato == lista_vertices[i].get_dato():
                return True
        return False

    """——————————————————————02——————————————————————ARISTAS—————————————————————————————————————————————————————————"""

    def ingresar_arista(self, origen, destino, peso):
        # verifica que el origen y destino existan #
        if not self.verificar_lista_arista(origen, destino, self.lista_aristas):
            # Ingresa en caso que no exista previamente  #
            if self.existe_vertice(origen, self.lista_vertices) and self.existe_vertice(destino, self.lista_vertices):
                self.lista_aristas.append(Arista(origen, destino, peso))
                # Adición del vértice a los adyacentes #
                self.obtener_vertice(origen, self.lista_vertices).get_lista_adyacentes().append(destino)
                return True
        return False

    def verificar_lista_arista(self, origen, destino, lista):

        for i in range(len(lista)):
            if origen == lista[i].get_origen() and destino == lista[i].get_destino():
                return True
        return False

    def mostrar_aristas(self):
        if len(self.lista_vertices) == 0:
            print('[ — ]')
            return False
        for i in range(len(self.lista_aristas)):
            self.lista_aristas[i].to_String()
        return True

    def mostrar_adyacencias(self):
        for i in range(len(self.lista_vertices)):
            print("| vértice: {0} |  Adyacencias: {1} |"
                  .format(self.lista_vertices[i].get_dato(),
                          self.lista_vertices[i].getListaAdyacencias()))

    """——————————————————————03——————————————————————FUNCIONES———————————————————————————————————————————————————————"""

    # Function 01
    @staticmethod
    def ordenar(aristas_copia):
        if len(aristas_copia) == 0:
            print('Grafo sin aristas.')
            return

        for i in range(len(aristas_copia)):
            for j in range(len(aristas_copia)):
                if aristas_copia[j].get_peso() < aristas_copia[i].get_peso():
                    temp = aristas_copia[i]
                    aristas_copia[i] = aristas_copia[j]
                    aristas_copia[j] = temp

    def grado_vertices(self):
        l = []
        for vertice in self.lista_vertices:
            g = 0
            for arista in self.lista_aristas:
                if arista.get_origen() == vertice.get_dato() or arista.get_destino() == vertice.get_dato():
                    g += 1
            l.append(g)
        return l

    def mayor_grado(self):
        l = self.grado_vertices()
        if len(l) == 0:
            print('Lista vacía')
            return
        # Lista con el último
        max = l[len(l) - 1]
        for e in l:
            if e > max:
                max = e
        return l.index(max)

    def prom_adyacencias(self):
        s = 0
        for i in self.grado_vertices():
            s += i
        return (s/len(self.grado_vertices()))

    def existen_pozos(self):
        pozos = []
        for vertice in self.lista_vertices:
            if len(vertice.lista_adyacentes) == 0:
                pozos.append(vertice)
        return pozos

    def existen_fuentes(self):
        fuentes = []
        destinos = []
        for vertice in self.lista_vertices:
            for adyace in vertice.lista_adyacentes:
                destinos.append(adyace)
        for vertice in self.lista_vertices:
            c = 0
            for destino in destinos:
                if vertice.get_dato() == destino:
                    c += 1
            if c == 0:
                fuentes.append(vertice)

        return fuentes

    def prom_pesos(self):
        print('Function')

    def mayor_arista(self):
        print('Function')

    def menor_arista(self):
        print('Function')

    def cantidad_adyacencias(self):
        print('Function')

    def adyacencias_grafo(self):
        print('Function')

    def vertices_no_adyacentes(self):
        print('Function')

    def adyacencia_comun(self):
        print('Function')

    """——————————————————————03——————————————————————ALGORITMOS——————————————————————————————————————————————————————"""

    @staticmethod
    def hacer_dirigido(aristas_copia):
        for arista in aristas_copia:
            for i in range(len(aristas_copia)):
                if arista.get_origen() == aristas_copia[i].get_destino() \
                        and arista.get_destino() == aristas_copia[i].get_origen():
                    aristas_copia.pop(i)
                    break
