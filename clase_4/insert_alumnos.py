import sqlite3


def main():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()

    while True:
        print("Insertar alumnos:")
        #id = input("Ingrese ID: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        nota = input("Ingrese nota: ")
        edad = input("Ingrese edad: ")

        cursor.execute(
            "INSERT INTO alumnos VALUES (?,?,?,?)",
            (nombre, apellido, nota, edad)
        )

        conn.commit()
        print("Alumno ingresado")
        r = input("Desea ingresar un nuevo alumno? (s/n):")
        if r == "s":
            continue
        else:
            break

    print(" ")

    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    print("Listado de alumnos:")
    print("---------------------------------------")
    for id, nombre, apellido, nota, edad in alumnos:
        print("{} | {} | {} | {} | {}".format(
            id, nombre, apellido, nota, edad
        ))

    conn.close()


if __name__ == '__main__':
    main()
