#proyecto 3
#crera un proycto que permita gestionar calificacones colocando un menu de opciones para agregar, mostrar y calcular promedios de las calificaciones

#notas 
#1 utilizar funciones y mandar llamar desde otro archivo 
#2 utilizar listas para almacebnar el nombre de un alumno y 3 calificaciones

def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_pricpal():
    print("\n\t..::: Sistema de Gestión de Calificacones  :::...\n\n 🅰️1.- Agregar  \n 🅱️2.- Mostrar \n 👌3.- Calcular Promedio  \n 👋4.- SALIR ")
    opcion=input("\t 🤙Elige una opción (1-4):  ").upper()
    return opcion  

def agrearCalificaciones(lista):
    nombre = input("\n\t Ingresa el nombre del alumno: ")
    calificaciones = []
    for i in range(5):
        calificacion = float(input(f"\t Ingresa la calificación {i+1} de {nombre}: "))
        calificaciones.append(calificacion)
    lista.append([nombre] + calificaciones)
    print(f"\n\t Calificaciones de {nombre} agregadas exitosamente.")
    esperarTecla()
    return lista


def mostrarCalificaciones(lista):

    if not lista:
        print("\n\t No hay calificaciones registradas.")
    else:
        print("\n\t Calificaciones Registradas:")
        for alumno in lista:
            print(f"\t {alumno[0]}: {alumno[1:]}")
    esperarTecla()


def CalcularPromedios(lista):
    
    if not lista:
        print("\n\t No hay calificaciones registradas.")
    else:
        print("\n\t Promedios de Calificaciones:")
        for alumno in lista:
            nombre = alumno[0]
            calificaciones = alumno[1:]
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"\t {nombre}: {promedio:.2f}")
    esperarTecla()