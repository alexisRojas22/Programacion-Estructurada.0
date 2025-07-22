import os
import mysql.connector

# Configuración de la conexión a la base de datos
config = {
    'user': 'root',          # Usuario de MySQL
    'password': '',          # Contraseña de MySQL
    'host': 'localhost',     # Servidor (localhost en este caso)
    'database': 'bd_peliculas'  # Nombre de la base de datos
}

def conectar():
    return mysql.connector.connect(**config)

def esperatecla():
    input("\n\t...Oprime cualquier tecla para continuar...")

def borrarpantalla():
    os.system("cls")

def crearpelicula():
    borrarpantalla()
    print("\t\t..::Crear Película::.. \n")
    
    nombre = input("Ingresa el nombre: ").lower().strip()
    categoria = input("Ingresa la categoría: ").lower().strip()
    clasificacion = input("Ingresa la clasificación: ").lower().strip()
    genero = input("Ingresa el género: ").lower().strip()
    idioma = input("Ingresa el idioma: ").lower().strip()
    
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
    valores = (nombre, categoria, clasificacion, genero, idioma)
    cursor.execute(query, valores)
    conexion.commit()
    print("\t\t..::La película se ha guardado en la base de datos::..")
    cursor.close()
    conexion.close()

def borrarpelicula():
    borrarpantalla()
    print("\n\t::: Borrar Películas :::\n")
    
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    
    if peliculas:
        print("\tPelículas disponibles:\n")
        for peli in peliculas:
            print(f"\tID: {peli['id']} - {peli['nombre']}")
        
        id_pelicula = input("\nIngresa el ID de la película a borrar: ")
        resp = input("¿Seguro que quieres borrar esta película? (si/no) ").lower().strip()
        
        if resp == "si":
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id_pelicula,))
            conexion.commit()
            print("\t\t..::La película se ha borrado correctamente::..")
    else:
        print("\n\t\tNo hay películas en la base de datos")
    
    cursor.close()
    conexion.close()

def mostrarpelicula():
    borrarpantalla()
    print("..::Mostrar Películas::.. ")
    
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM peliculas")
    peliculas = cursor.fetchall()
    
    if peliculas:
        for peli in peliculas:
            print("\n\tDatos de la película:")
            for clave, valor in peli.items():
                print(f"\t{clave}: {valor}")
    else:
        print("\n\t\tNo hay películas en la base de datos")
    
    cursor.close()
    conexion.close()

def agregarcaracteristicapelicula():
    borrarpantalla()
    print("\t\t..::Agregar característica a la Película::.. ")
    
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    
    if peliculas:
        print("\tPelículas disponibles:\n")
        for peli in peliculas:
            print(f"\tID: {peli['id']} - {peli['nombre']}")
        
        id_pelicula = input("\nIngresa el ID de la película a modificar: ")
        cursor.execute("DESCRIBE peliculas")
        columnas = [columna[0] for columna in cursor.fetchall()]
        
        print("\n\tColumnas disponibles (no se puede modificar 'id'):")
        for col in columnas:
            if col != 'id':
                print(f"\t{col}")
        
        columna = input("\nIngresa el nombre de la columna a modificar: ")
        if columna in columnas and columna != 'id':
            nuevo_valor = input(f"Ingresa el nuevo valor para '{columna}': ").strip()
            
            query = f"UPDATE peliculas SET {columna} = %s WHERE id = %s"
            cursor.execute(query, (nuevo_valor, id_pelicula))
            conexion.commit()
            print("\t\t..::La característica se ha actualizado::..")
    
    cursor.close()
    conexion.close()

def modificarcaracteristicapelicula():
    borrarpantalla()
    print("\n\t:::Modificar alguna caracteristica de la Película:::\n")
    
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    
    if peliculas:
        print("\tPelículas disponibles:\n")
        for peli in peliculas:
            print(f"\tID: {peli['id']} - {peli['nombre']}")
        
        id_pelicula = input("\nIngresa el ID de la película a modificar: ")
        cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_pelicula,))
        pelicula = cursor.fetchone()
        
        if pelicula:
            print("\n\tCaracterísticas actuales:")
            for clave, valor in pelicula.items():
                print(f"\t{clave}: {valor}")
            
            columna = input("\nIngresa el nombre de la característica a modificar: ")
            if columna in pelicula and columna != 'id':
                nuevo_valor = input(f"Ingresa el nuevo valor para '{columna}': ").strip()
                
                query = f"UPDATE peliculas SET {columna} = %s WHERE id = %s"
                cursor.execute(query, (nuevo_valor, id_pelicula))
                conexion.commit()
                print("\t\t..::La característica se ha actualizado::..")
                
                cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_pelicula,))
                pelicula_actualizada = cursor.fetchone()
                print("\n\tPelícula actualizada:")
                for clave, valor in pelicula_actualizada.items():
                    print(f"\t{clave}: {valor}")
    
    cursor.close()
    conexion.close()
    esperatecla()

def borrarcaracteristicapeliculas():
    borrarpantalla()
    print("\n\tBorrar alguna caracteristica de la pelicula")
    
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM peliculas")
    peliculas = cursor.fetchall()
    
    if peliculas:
        print("\tPelículas disponibles:\n")
        for peli in peliculas:
            print(f"\tID: {peli['id']} - {peli['nombre']}")
        
        id_pelicula = input("\nIngresa el ID de la película a modificar: ")
        cursor.execute("DESCRIBE peliculas")
        columnas = [columna[0] for columna in cursor.fetchall()]
        
        print("\n\tColumnas que se pueden borrar (establecer a NULL):")
        columnas_borrables = []
        for col in columnas:
            if col != 'id':
                columnas_borrables.append(col)
                print(f"\t{col}")
        
        columna = input("\nIngresa el nombre de la columna a borrar (establecer a NULL): ")
        if columna in columnas_borrables:
            query = f"UPDATE peliculas SET {columna} = NULL WHERE id = %s"
            cursor.execute(query, (id_pelicula,))
            conexion.commit()
            print(f"\t\t..::La columna '{columna}' se ha establecido a NULL::..")
            
            cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_pelicula,))
            pelicula_actualizada = cursor.fetchone()
            print("\n\tPelícula actualizada:")
            for clave, valor in pelicula_actualizada.items():
                print(f"\t{clave}: {valor}")
    
    cursor.close()
    conexion.close()
    esperatecla()