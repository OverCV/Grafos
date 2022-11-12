"""—————————————————
    Clase Grafo.
—————————————————"""


class Arista:

    """——————————————————————00——————————————————————CONSTRUCTOR—————————————————————————————————————————————————————"""
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.paso = True

    def get_origen(self):
        return self.origen

    def set_origen(self, origen):
        self.origen = origen

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_destino(self):
        return self.destino

    def set_destino(self, destino):
        self.destino = destino

    def get_paso(self):
        return self.paso

    def set_paso(self, paso):
        self.paso = paso

    def to_String(self):
        print('[ Arista: ', self.get_origen(), '→', self.get_destino(), ' | Peso: ', self.get_peso(), '| Paso', self.get_paso(), ']')
