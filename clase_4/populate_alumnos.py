import sqlite3


def main():
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


if __name__ == '__main__':
    main()
