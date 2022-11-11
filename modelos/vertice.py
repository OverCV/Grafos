"""——————————————————————————————————————————————
    Menú con métodos funcionales por consola.
——————————————————————————————————————————————"""


class Vertice:

    def __init__(self, dato):
        """
        dato: Puede tomar un valor variable para reconocer.
        lista_adyacentes: Lista con Aristas, cuáles cuentan con peso, un origen y destino.
        """
        self.dato = dato
        self.lista_adyacentes = []

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_lista_adyacentes(self):
        return self.lista_adyacentes

    def set_lista_adyacentes(self, lista_adyacentes):
        self.lista_adyacentes = lista_adyacentes
