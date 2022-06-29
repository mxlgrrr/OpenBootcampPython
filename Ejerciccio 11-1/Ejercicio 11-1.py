"""
    En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, 
    la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

    Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

    Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""
import sqlite3

conexion = sqlite3.connect('alumnos.db')
  
cursor = conexion.cursor()

cursor.execute("DROP TABLE IF EXISTS ALUMNOS")
  
tabla = """ CREATE TABLE ALUMNOS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre CHAR(25) NOT NULL,
            Apellido CHAR(25) NOT NULL
        ); """

cursor.execute(tabla)

listaAlumnos = [["Juan","Perez"],["Federico","Lopez"], ["Agustin","Vazquez"],["Vladimir","Tokarev"],["Mariano","Franzosi"],["Lucas","Cao"],["Juan","Palomo"],["John","Doe"]]

for elemento in listaAlumnos:
    insertarAlumno = f"""INSERT INTO ALUMNOS (Nombre, Apellido) VALUES ('{elemento[0]}', '{elemento[1]}');"""
    cursor.execute(insertarAlumno)
    conexion.commit()

cursor.execute("SELECT * FROM ALUMNOS WHERE Nombre = 'Vladimir';")
rows = cursor.fetchall()

for row in rows:
    print(f"Id: {row[0]} - Nombre Completo: {row[1]} {row[2]}") 

conexion.close()