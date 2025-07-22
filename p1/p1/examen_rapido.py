import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Películas :::...\n\n 1.- Crear \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar Característica \n 5.- Modificar Característica \n 6.- Borrar Característica \n 7.- SALIR ")
    opcion = input("\t\n Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del SW")
        case _:
            input("\n\tOpción inválida, vuelva a intentarlo... por favor")