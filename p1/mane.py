'''Proyecto 1 .
 crear un proyecto que permita gestionar(administrar) peliculas;colocar un menu de opciones para agregar, borrar, 
 modificar, consultar, buscara y vaciar peliculas
 Notas : 1.- utilizar funciones y mandara allamar deesde otro archivo 
         2.- Utilizar una diccionarios para almacenar los atributos o caracteristicas de un apelicula
'''
import Calificaciones

def main():

    opcion=True
    datos = []
    while opcion:
        Calificaciones.borra_pantalla()
        opcion=Calificaciones.menu_pricpal()

    match opcion: 
        case "1":
            Calificaciones.agrearCalificaciones(datos)
            Calificaciones.esperarTecla()
        case "2":
            Calificaciones.mostrarCalificaciones(datos)
            Calificaciones.esperarTecla() 
        case "3":
           Calificaciones.CalcularPromedios(datos)   
           Calificaciones.esperarTecla()
        case "4":
           opcion=False
           Calificaciones.borra_pantalla() 
           print("Terminaste la ejecucion del SW")
        
        case _:
            opcion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")

main()

if _name_ == "_main_":
    main()