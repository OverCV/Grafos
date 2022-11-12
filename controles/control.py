"""——————————————————————————————————————————————————————
    Menú por consola para operaciones sobre el Grafo.
——————————————————————————————————————————————————————"""
import sys, os, time, random
# sys.path.append('../')

# from helpers import Helpers
from modelos.grafo import Grafo
from modelos.algoritmo import Algoritmo

class Control:

    """—————————————————————————————————————————————CONSTRUCTOR——————————————————————————————————————————————————————"""

    def __init__(self):
        self.grafo = Grafo()
        self.algoritmos = Algoritmo('test', self.grafo)
        self.active = True

    """—————————————————————————————————————————————SALIDA-PANTALLA——————————————————————————————————————————————————"""

    def load(self):
        self.active = True
        while self.active:

            print(
                "\n▌ OPCIONES"
                "\n▌ 01 — Ejecución            02 — Ingresar vértice     03 — Ver vértices         04 — Generar vértice    ▐"
                "\n▌ 05 — Ingresar arista      06 — Generar arista       07 — Ver aristas          08 — Algoritmos         ▐"
                "\n▌   ∙∙∙   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   —   ∙∙∙   ∙∙∙     ▐"
                "\n▌ 09 — Ordenar ascendente   10 — Grado de vértices    11 — Vértice mayor grado  12 — Promedio (lst ady) ▐"
                "\n▌ 13 — Pozos                14 — Fuentes              15 — Prom. peso aristas   16 — Arista (peso-max)  ▐"
                "\n▌ 17 — Arista (peso-min)    18 — Vértice (num-ady)    19 — Ady. de vértices     20 — Get Grafo          ▐"
                "\n▌ 21 — Reset Grafo                                                                                      ▐"
                # ∙∙∙
                "\n▌ 00 — Volver                                                                                           ▐"
            )
            o = {
                1: self.exit,                2: self.ingresar_vertice, 3: self.ver_vertices,     4: self.generar_vertice,
                5: self.ingresar_arista,     6: self.generar_arista,   7: self.ver_aristas,      8: self.algoritmos,
                # ∙∙∙
                9: self.ordenar_ascendente, 10: self.lista_grados,    11: self.mayor_grado,     12: self.prom_ady,
                13: self.hay_pozos,         14: self.hay_fuentes,     15: self.default,         16: self.default,
                17: self.default,           18: self.default,         19: self.default,         20: self.get_grafo,
                21: self.reset_grafo,       22: self.default,
                # ∙∙∙
                0: self.exit
            }
            i = Helpers.read_int('Ingrese una opción: ', 'Opción inválida.', 0, 22)
            o[i]()

    def exit(self):
        self.active = False
        return

    @staticmethod
    def default():
        print('Opción no disponible.')

    """—————————————————————————————————————————————MÉTODOS——————————————————————————————————————————————————————————"""

    """———— ∙ ∙ ∙ ∙
        Vértices
    ∙ ∙ ∙ ∙ ————"""
    def ingresar_vertice(self):
        dato = input('Dato del vértice: ')
        self.grafo.ingresar_vertice(dato)

    def ver_vertices(self):
        print('Lista de vértices:')
        self.grafo.mostrar_vertices()

    def obtener_vertice(self):
        origen = input('Origen: ')
        lista = []
        self.grafo.obtener_vertice(origen, lista)

        print('Lista [vértices]: ', lista)

    def generar_vertice(self):
        # Rango entre 65 y 90 [A-Z] #
        c = random.randint(66, 89)
        i = random.randint(0, 9)
        dato = str(chr(c) + str(i))

        self.grafo.ingresar_vertice(dato)
        print('Vértice', dato, 'creado.')

    """———— ∙ ∙ ∙ ∙
        Aristas
    ∙ ∙ ∙ ∙ ————"""
    def ingresar_arista(self):
        origen = input('Origen de la arista: ')
        destino = input('Destino de la arista: ')
        peso = input('Peso de la arista: ')
        ok = self.grafo.ingresar_arista(origen, destino, peso)
        if not ok:
            print('No se creó la arista.')

    def generar_arista(self):
        lista_vertices = self.grafo.get_lista_vertices()

        l = len(lista_vertices)
        if l < 2:
            print('Vértices insuficientes.')
            return
        i = random.randint(0, l-1)
        j = random.randint(0, l-1)
        origen = lista_vertices[i].get_dato()
        destino = lista_vertices[j].get_dato()

        # print('destino', destino, ' | origen', origen)
        peso = (i+1)*(j+1)

        if i == j:
            self.generar_arista()
        else:
            if self.grafo.ingresar_arista(origen, destino, peso):
                print('Arista creada: [', origen, ' → ', destino, '| W: ', peso, ']')
                return
            print('Arista fallida: [', origen, ' → ', destino, '|   W: ', peso, ']')

    def ver_aristas(self):
        print('Lista de aristas:')
        self.grafo.mostrar_aristas()

    """———— ∙ ∙ ∙ ∙ ∙
        Algoritmo
    ∙ ∙ ∙ ∙ ∙ ————"""
    def algoritmos(self):
        lista_aristas = self.grafo.get_lista_aristas()

        if len(lista_aristas) == 0:
            print('Grafo insuficiente.')
            return

        o = {
            'p': self.algoritmos.prim, 'd': Algoritmos.dijkstra,
            'k': Algoritmos.kruskal, 'b': Algoritmos.boruvka
        }
        i = (input('Ingrese el nombre del algoritmo a ejecutar: ').lower())[0]

        if i != 'p' and i != 'd' and i != 'k' and i != 'b':
            print('Algoritmo inexistente')
            return

        conjunto = o[i](self.algoritmos)

        print(conjunto)

    def algoritmo_i(self, i):
        if i == 0 or i == 5:
            print('Invalid index (0 | 5).')
            return None
        lista_aristas = self.grafo.get_lista_aristas()

        if len(lista_aristas) == 0:
            print('Grafo insuficiente.')
            return

        o = {
            1: Algoritmos.prim, 2: Algoritmos.dijkstra, 3: Algoritmos.kruskal, 4: Algoritmos.boruvka,
            6: Algoritmos.anchura, 7: Algoritmos.profundidad, 8: Algoritmos.floyd_warshall, 9: Algoritmos.ford_fulkerson
        }

        # Retorno de 02 conjuntos | Conjunto de vértices y Conjunto de aristas.
        conjuntos = o[i](self.algoritmos)

        return conjuntos

        # self.grafo.alg_prim()

    """———— ∙ ∙ ∙
        Extras
    ∙ ∙ ∙ ————"""
    def ordenar_ascendente(self):
        lista_aristas = self.grafo.get_lista_aristas()

        self.grafo.ordenar(lista_aristas)
        print('El grafo ha sido ordenado de forma ascendente.')

    def lista_grados(self):
        lista_vertices = self.grafo.get_lista_vertices()

        if len(lista_vertices) == 0:
            print('Grafo sin vértices [lista_grados].')
            return
        l = self.grafo.grado_vertices()
        for i in range(len(l)):
            # print('i:', i)
            # print('vértice:', self.lista_vertices[i].get_dato())
            # print('list[g]:', l[i])
            print('El vértice', lista_vertices[i].get_dato(), 'tiene grado', l[i])

    def mayor_grado(self):
        lista_vertices = self.grafo.get_lista_vertices()

        if len(lista_vertices) == 0:
            print('Grafo sin vértices [mayor_grado].')
            return
        i = self.grafo.mayor_grado()
        l = self.grafo.grado_vertices()
        print('El vértice de mayor grado es', lista_vertices[i].get_dato(), ', sea', l[i], 'su grado.')

    def prom_ady(self):
        p = self.grafo.prom_adyacencias()
        print('Promedio de las adyacencias al grafo:', p)

    def hay_pozos(self):
        pozos = self.grafo.existen_pozos()
        if len(pozos) == 0:
            print('No hay pozos')
            return
        for pozo in pozos:
            print('Se encontró un poso, cual es el vértice', pozo.get_dato(), '.')

    def hay_fuentes(self):
        lista_vertices = self.grafo.get_lista_vertices()

        if len(lista_vertices) == 0:
            print('Grafo insuficiente.')
        fuentes = self.grafo.existen_fuentes()
        if len(fuentes) == 0:
            print('No hay fuentes')
            return
        for fuente in fuentes:
            print('El vértice', fuente.get_dato(), 'es una fuente.')

    def grafo_random(self):
        lista_vertices = self.grafo.get_lista_vertices()

        vertices = []
        for i in range(len(lista_vertices)):
            r = random.randint(0, 1)
            if r == 0:
                vertices.append(True)
                pass
            vertices.append(False)
        print(vertices)

    def reset_grafo(self):
        """
        Esta función elimina el grafo actual para dar paso a la creación de uno propio.
        """
        lista_vertices = self.grafo.get_lista_vertices()

        for vertice in lista_vertices:
            vertice.set_lista_adyacentes([])
        self.grafo.set_lista_vertices([])
        self.grafo.set_lista_aristas([])
        print('Reset has been successful.')

    def get_grafo(self):
        self.grafo.ingresar_vertice('Librería Euler')
        self.grafo.ingresar_vertice('Librería Gadner')
        self.grafo.ingresar_vertice('Librería Könisberg')
        self.grafo.ingresar_vertice('Librería Voronoi')
        self.grafo.ingresar_vertice('Librería Gauss')
        self.grafo.ingresar_vertice('Casita')
        self.grafo.ingresar_vertice('Librería Richter')
        self.grafo.ingresar_vertice('Librería Fibonacci')
        self.grafo.ingresar_vertice('Librería Fahrenheit')
        self.grafo.ingresar_vertice('Librería Hilbert')
        self.grafo.ingresar_vertice('Librería Celsius')

        # Euler
        self.grafo.ingresar_arista('Librería Euler', 'Librería Gadner', 415)
        self.grafo.ingresar_arista('Librería Gadner', 'Librería Euler', 415)

        self.grafo.ingresar_arista('Librería Euler', 'Librería Voronoi', 317)
        self.grafo.ingresar_arista('Librería Voronoi', 'Librería Euler', 317)

        self.grafo.ingresar_arista('Librería Euler', 'Casita', 330)
        self.grafo.ingresar_arista('Casita', 'Librería Euler', 330)

        self.grafo.ingresar_arista('Librería Euler', 'Librería Gauss', 230)
        self.grafo.ingresar_arista('Librería Gauss', 'Librería Euler', 230)

        self.grafo.ingresar_arista('Librería Euler', 'Librería Könisberg', 300)
        self.grafo.ingresar_arista('Librería Könisberg', 'Librería Euler', 300)

        # Gadner
        self.grafo.ingresar_arista('Librería Gadner', 'Librería Fibonacci', 310)
        self.grafo.ingresar_arista('Librería Fibonacci', 'Librería Gadner', 310)

        self.grafo.ingresar_arista('Librería Gadner', 'Librería Voronoi', 170)
        self.grafo.ingresar_arista('Librería Voronoi', 'Librería Gadner', 170)

        # Voronoi
        self.grafo.ingresar_arista('Librería Voronoi', 'Librería Fibonacci', 299)
        self.grafo.ingresar_arista('Librería Fibonacci', 'Librería Voronoi', 299)

        self.grafo.ingresar_arista('Librería Voronoi', 'Casita', 190)
        self.grafo.ingresar_arista('Casita', 'Librería Voronoi', 190)

        # Gauss
        self.grafo.ingresar_arista('Librería Gauss', 'Casita', 330)
        self.grafo.ingresar_arista('Casita', 'Librería Gauss', 330)

        self.grafo.ingresar_arista('Librería Gauss', 'Librería Fahrenheit', 330)
        self.grafo.ingresar_arista('Librería Fahrenheit', 'Librería Gauss', 330)

        self.grafo.ingresar_arista('Librería Gauss', 'Librería Richter', 198)
        self.grafo.ingresar_arista('Librería Richter', 'Librería Gauss', 198)

        self.grafo.ingresar_arista('Librería Gauss', 'Librería Könisberg', 198)
        self.grafo.ingresar_arista('Librería Könisberg', 'Librería Gauss', 198)

        # Könisberg
        self.grafo.ingresar_arista('Librería Könisberg', 'Librería Richter', 198)
        self.grafo.ingresar_arista('Librería Richter', 'Librería Könisberg', 198)

        self.grafo.ingresar_arista('Librería Könisberg', 'Librería Celsius', 198)
        self.grafo.ingresar_arista('Librería Celsius', 'Librería Könisberg', 198)

        # Casita
        self.grafo.ingresar_arista('Casita', 'Librería Fibonacci', 345)
        self.grafo.ingresar_arista('Librería Fibonacci', 'Casita', 345)

        self.grafo.ingresar_arista('Casita', 'Librería Fahrenheit', 180)
        self.grafo.ingresar_arista('Librería Fahrenheit', 'Casita', 180)

        # Richter
        self.grafo.ingresar_arista('Librería Richter', 'Librería Fahrenheit', 267)
        self.grafo.ingresar_arista('Librería Fahrenheit', 'Librería Richter', 267)

        self.grafo.ingresar_arista('Librería Richter', 'Librería Celsius', 280)
        self.grafo.ingresar_arista('Librería Celsius', 'Librería Richter', 280)

        # Fibonacci
        self.grafo.ingresar_arista('Librería Fibonacci', 'Librería Hilbert', 250)
        self.grafo.ingresar_arista('Librería Hilbert', 'Librería Fibonacci', 250)

        self.grafo.ingresar_arista('Librería Fibonacci', 'Librería Fahrenheit', 450)
        self.grafo.ingresar_arista('Librería Fahrenheit', 'Librería Fibonacci', 450)

        # Fahrenheit
        self.grafo.ingresar_arista('Librería Fahrenheit', 'Librería Hilbert', 230)
        self.grafo.ingresar_arista('Librería Hilbert', 'Librería Fahrenheit', 230)

        self.grafo.ingresar_arista('Librería Fahrenheit', 'Librería Celsius', 255)
        self.grafo.ingresar_arista('Librería Celsius', 'Librería Fahrenheit', 255)

        # Hilbert
        self.grafo.ingresar_arista('Librería Hilbert', 'Librería Celsius', 312)
        self.grafo.ingresar_arista('Librería Celsius', 'Librería Hilbert', 312)

        print('Librería ACME generada.')
        return
