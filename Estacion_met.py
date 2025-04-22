import random
from Ciudad import NodoCiudad
from Horas import NodoHora

class EstacionMeteorologica:
    def __init__(self):
        self.cabeza = None

    def agregar_ciudad(self, ciudad):
        nuevo_nodo = NodoCiudad(ciudad)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def agregar_datos_hora(self, ciudad, hora, temperatura, humedad, viento):
        actual = self.cabeza
        while actual:
            if actual.ciudad == ciudad:
                nuevo_nodo_hora = NodoHora(hora, temperatura, humedad, viento)
                if not actual.horas:
                    actual.horas = nuevo_nodo_hora
                else:
                    actual_hora = actual.horas
                    while actual_hora.siguiente:
                        actual_hora = actual_hora.siguiente
                    actual_hora.siguiente = nuevo_nodo_hora
                return
            actual = actual.siguiente

    def mostrar_datos(self):
        actual = self.cabeza
        while actual:
            print(f"Ciudad: {actual.ciudad}")
            actual_hora = actual.horas
            while actual_hora:
                print(f"  Hora: {actual_hora.hora}, Temperatura: {actual_hora.temperatura}°C, Humedad: {actual_hora.humedad}%, Viento: {actual_hora.viento} km/h")
                actual_hora = actual_hora.siguiente
            actual = actual.siguiente

def generar_datos_aleatorios():
    ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
    horas = ["06:00", "12:00", "18:00", "00:00"]
    estacion = EstacionMeteorologica()
    for ciudad in ciudades:
        estacion.agregar_ciudad(ciudad)
        for hora in horas:
            temperatura = round(random.uniform(-5, 40), 1)  # Temperatura entre -5 y 40 °C
            humedad = random.randint(10, 100)  # Humedad entre 10% y 100%
            viento = random.randint(0, 100)  # Viento entre 0 y 100 km/h
            estacion.agregar_datos_hora(ciudad, hora, temperatura, humedad, viento)
    return estacion
