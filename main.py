"""———————————————————————————————————————
    Clase inicializadora del proyecto.
———————————————————————————————————————"""
from controles.control import Control

def main():
    controlador = Control()
    controlador.init()


if __name__ == '__main__':
    main()
