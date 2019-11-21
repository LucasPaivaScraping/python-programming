import sqlite3


def main():
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos")
    # Listar alumnos
    alumnos = cursor.fetchall()
    print("Listado de alumnos:")
    print("---------------------------------------")
    for id, nombre, apellido, nota, edad in alumnos:
        print("{} | {} | {} | {} | {}".format(
            id, nombre, apellido, nota, edad
        ))

    print(" ")
    print(" ")
    print("Eliminar alumno: ")

    id = input("Ingrese el id del alumno a eliminar: ")
    cursor.execute(
        "DELETE FROM alumnos where id = ?",
        (id)
    )
    conn.commit()
    print("Alumno actualizado!!.")
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
