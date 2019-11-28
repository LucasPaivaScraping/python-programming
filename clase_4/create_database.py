# Libreria para usar bases de datos sqlLite
import sqlite3


def main():
    """
    Funcion principal encierra todo el codigo prinicipal del modulo
    """
    # Creo la base alumnos y establece la conexion
    conn = sqlite3.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE alumnos (id INTEGER AUTONUMERIC PRIMARY KEY NOT NULL, 
                    nombre TEXT, apellido TEXT, nota NUMERIC, edad NUMERIC)
                    """)

    print("Tabla Alumnos creada!")

    # Cerramos conexion
    conn.close()


if __name__ == "__main__":
    main()







