"""
Modulo de funciones para importar como modulo desde otros modulos
"""
import sqlite3
import sys


def imprimir_menu():
    """
    Funcion que simplemente muestra un menu por pantalla
    :return:
    """
    print("ABM de ALUMNOS:")
    print("Menú de opciones:")
    print("----------------------------------------------------")
    print("1) Crear base de datos .")
    print("2) Popular tabla.")
    print("3) Listar alumnos.")
    print("4) Agregar alumno.")
    print("5) Actualizar alumno.")
    print("6) Eliminar alumno.")
    print("7) Salir.")
    print("----------------------------------------------------")
    print(" ")
    return int(input("- Ingrese una opción: "))


def create_database():
    """
    Funcion que crea la base de datos
    """
    try:
        conn = sqlite3.connect("alumnos.db")
        cursor = conn.cursor()
        cursor.execute("""
                            CREATE TABLE alumnos (id NUMERIC, nombre TEXT, apellido TEXT, nota NUMERIC, edad NUMERIC)
                            """)

        print("Tabla Alumnos creada!")
        conn.close()
    except sqlite3.OperationalError:
        print("La base de datos ya fue creada! .")


def populate_database():
    """
    Funcion que carga datos por primera vez automaticamente
    """
    # se establece conexion con la BD y abro cursor
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    # creo una tupla de tuplas para agregar registros a la tabla
    alumnos = (
        (1, "Juan", "Granizado", 8, 25),
        (2, "Esteban", "Quito", 2, 19),
        (3, "Marina", "Cordoba", 10, 25),
    )

    for alumno in alumnos:
        cursor.execute("INSERT INTO alumnos VALUES (?, ?, ?, ?, ?)", alumno)

    # Para que se agreguen los registros efectivamente tenemos que hacer commit
    conn.commit()

    print("Datos cargados!")

    # Cerramos conexion
    conn.close()


def listar_alumnos():
    """
    Funcion que lista todos los alumnos
    """
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    print("Listado de alumnos:")
    print("---------------------------------------")
    for id, nombre, apellido, nota, edad in alumnos:
        print("{} | {} | {} | {} | {}".format(
            id, nombre, apellido, nota, edad
        ))


def insert_alumnos():
    """
    Funion que permite insertar nuevo registro por consola
    """
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    while True:
        print("Insertar alumnos:")
        id = input("Ingrese ID: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        nota = input("Ingrese nota: ")
        edad = input("Ingrese edad: ")

        cursor.execute(
            "INSERT INTO alumnos VALUES (?,?,?,?,?)",
            (id, nombre, apellido, nota, edad)
        )

        conn.commit()
        print("Alumno ingresado")
        r = input("Desea ingresar un nuevo alumno? (s/n):")
        if r == "s":
            continue
        else:
            break


def update_alumnos():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    print("Actualizar notas: ")
    id = input("Ingrese el id del alumno a actualizar: ")
    nueva_nota = input("Ingrese la nueva nota: ")
    cursor.execute(
        "UPDATE alumnos SET nota = ? where id = ?",
        (nueva_nota, id)
    )

    # SQL Injection
    # cursor.executescript(
    #    "UPDATE alumnos SET nota = {} where id = {}".format(
    #        nueva_nota, id
    #    )
    # )

    conn.commit()
    print("Alumno actualizado!!.")
    print(" ")


def delete_alumnos():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    print("Eliminar alumno: ")

    id = input("Ingrese el id del alumno a eliminar: ")
    cursor.execute(
        "DELETE FROM alumnos where id = ?",
        (id)
    )
    conn.commit()
    print("Alumno Eliminado!!.")


def salir():
    sys.exit()