"""
Esto es un dosctring, comentarios multilinea, por convencion si se requiere incluir informacion respecto al modulo se
lo agrega aqui.
Este archivio main.py es el principal , lo cual deberia sere el primero a ejecutarse.
"""

# Ejemplo importando modulo (es decir un archivo .py)
#from functions import imprimir_menu, create_database, populate_database, listar_alumnos, insert_alumnos, update_alumnos, delete_alumnos, salir
#from functions import *

# Ejemplo importando un package o paquete, es decir una carpeta que dentro contiene modulos
from utils.functions import *


def main():
    """
    Funcion main donde va el codigo principal
    :return:
    """
    while True:
        op = imprimir_menu()
        print(" ")
        if op != 7:
            if op == 1:
                # Crear base de datos
                create_database()
                print(" ")
            elif op == 2:
                # Insertar registros iniciales
                populate_database()
                print(" ")
            elif op == 3:
                # Listar tabla
                listar_alumnos()
                print(" ")
            elif op == 4:
                # Insertar regitros por consola
                insert_alumnos()
                # Luego de insertar llamo a la funcion listar para mostrar un resultado
                print(" ")  # Este print es solo para dejar un espacio
                listar_alumnos()
                print(" ")
            elif op == 5:
                # Actualizar alumnos
                listar_alumnos()
                print(" ")
                update_alumnos()
                print(" ")
                listar_alumnos()
                print(" ")
            elif op == 6:
                # Eliminar alumnos
                listar_alumnos()
                print(" ")
                delete_alumnos()
                print(" ")
                listar_alumnos()
                print(" ")
            else:
                print("Debe ingresar una opción valida")
                print("xxx")
                imprimir_menu()
                print(" ")
        else:
            break
    salir()


if __name__ == '__main__':
    main()