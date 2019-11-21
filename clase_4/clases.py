"""
classes
"""
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self):
        print("Hola ! mi nombre es {}".format(self.nombre))

class Auto:

    _encendido = False
    _velocidad = 0

    def __init__(self, color, puertas, litros_nafta):
        self.color = color
        self.puertas = puertas
        self.tanque = litros_nafta

    def encender(self):
        self._encendido = True

    def apagar(self):
        self._encendido = False

    def acelerar(self):
        if self._encendido:
            self._velocidad += 10
        else:
            print("El auto esta apagado!")

    def frenar(self):
        self._velocidad -= 10

    def esta_encendido(self):
        return self._encendido

    def velocidad_actual(self):
        return self._velocidad