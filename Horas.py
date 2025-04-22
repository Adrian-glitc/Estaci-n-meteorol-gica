class NodoHora:
    def __init__(self, hora, temperatura, humedad, viento):
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.siguiente = None