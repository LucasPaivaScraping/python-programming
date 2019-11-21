import sqlite3


def main():
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




if __name__ == '__main__':
    main()
