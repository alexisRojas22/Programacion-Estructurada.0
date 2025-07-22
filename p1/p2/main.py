import atletsimo
opcion=True
while opcion:
    atletsimo.borrarpantalla()
    print("\n\t\t\t..::: Menu de Atletismo :::... \n\t\t 1. Inserta los Datos de tu Entrenamiento " \
    "\n\t\t 2. Retos Semanales \n\t\t 3. Mostrar historial tu entrenamiento \n\t\t 4. Resumen del Entrenamiento " \
    "\n\t\t 5. Editar un dato\n\t\t 6. Borrar Todo \n\t\t 7. Salir del Programa")
    opcion=input("\n\t\t Elige una opción: ").upper().strip()

    match opcion:
        case "1":
            atletsimo.tiempodatos()
            atletsimo.esperatecla() 
        case "2":
            atletsimo.retosdatos()
            atletsimo.esperatecla()   
        case "3":
            atletsimo.historialdatos() 
            atletsimo.esperatecla()
        case "4": 
            atletsimo.resumendatos()
            atletsimo.esperatecla()
        case "5": 
            atletsimo.editardatos()
            atletsimo.esperatecla()
        case "6":
            atletsimo.vaciardatos()
            atletsimo.esperatecla()
        case "7":
            opcion=False    
            atletsimo.borrarpantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            opcion=True 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor") 
