"""
classes
"""
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self):
        print("Hola ! mi nombre es {}".format(self.nombre))

    def hablar(self, mensaje):
        print("{} dice - {}".format(self.nombre, mensaje))    

    def __hablar(self, mensaje):
        print("{} dice - {}".format(self.nombre, mensaje))

class Auto:

    encendido = False
    velocidad = 0

    def __init__(self, color, puertas, litros_nafta):
        self.color = color
        self.puertas = puertas
        self.tanque = litros_nafta

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False

    def acelerar(self):
        if self.encendido:
            self.velocidad += 10
            self.tanque -= 10
        else:
            print("El auto esta apagado!")

    def frenar(self):
        self.velocidad -= 10

    def esta_encendido(self):
        return self.encendido

    def velocidad_actual(self):
        return self.velocidad