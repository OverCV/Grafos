"""——————————————————————————————————————————————
    Controlador de los distintos componentes.
——————————————————————————————————————————————"""
import sys , os, time, random
# scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
# os.chdir(scriptPath)
# sys.path.append('../')

from controles.menu import Menu
from vistas.interfaz import Interfaz
from controles.helpers import Helpers



class Control:
    """
    Esta clase dicta a la interfaz y el menú de opciones vía consola, cargará esencialmente los recursos desde la clase
    Menú cuál hace manejo del Grafo, con ellos ha de definirse una ruta para la ejecución, desde esta misma se propor-
    cionarán los recursos iniciales para un manejo efectivo entre [Menu] e [Interface].

    Se definen entonces objetivos como:
        * Comunicación entre clases:
            Creación de ciclo ejecutable desde dónde se brindará el (estado) de Menú, este será el momento presente del
            manejo del grafo con lo que se actualizará para dar dicha información para su visualización desde
            [Interface].
    """
    def __init__(self):
        self.name = 'ACME'
        self.menu = Menu()
        self.interfaz = Interfaz(self.menu)

    def init(self):
        """
        Inicio en selección de opciones.
        :return: salir será la salida estándar.
        """
        while True:
            print('▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
                  '▌▓▒░     01. Iniciar     ░▒▓█▓▒░     02. Opciones     ░▒▓█▓▒░     00. Salir     ░▒▓▐\n' \
                  '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟')    

            o = {
                1: self.run, 2: self.menu.load, 0: self.salir
            }
            i = Helpers.read_int("Ingrese una opción: ", "Opción inválida.", 0, 2)
            o[i]()

    @staticmethod
    def salir():
        s = '▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                       ¡GRACIAS POR USAR EL PROGRAMA!                      ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                             Desarrollado por:                             ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                           Eliana Gallego Rivera.                          ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                      Cristian David Gonzales Castaño.                     ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                          Lina María Nieto Alarcón.                        ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟'
        print(s)
        sys.exit()

    """——————————————————————01——————————————————————EJECUCIÓN———————————————————————————————————————————————————————"""

    def run(self):

        print('▌▓▒░    Inicio ∙∙∙')

        """———— ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙
            Variables iniciales
        ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ————————"""
        timer = 0
        # Obtención del grafo para dar trabajo.
        # self.control.get_grafo()

        while True:
            # print('▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
            #       '▌▓▒░    01. Visualizar    ░▒▓█▓▒░    02. Opciones    ░▒▓█▓▒░     00. Volver     ░▒▓▐\n' \
            #       '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟')

            # o = {1: self.interface.main_menu, 2: self.control.load, 0: self.init}
            # i = Helpers.read_int("Ingrese una opción: ", "Opción inválida.", 0, 2)
            # o[i]()
            self.interfaz.main_menu()
            self.salir()