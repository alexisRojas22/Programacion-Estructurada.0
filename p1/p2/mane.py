
import agenda

def main():

    opcion=True
    datos = []
    while opcion:
        agenda.borra_pantalla()
        opcion=agenda.menu_pricpal()

    match opcion: 
        case "1":
            agenda.agregar_contacto(datos)
            agenda.esperarTecla()
        case "2":
            agenda.mostrar_todos_los_contactos(datos)
            agenda.esperarTecla() 
        case "3":
           agenda.buscar_contacto_por_nombre(datos)   
           agenda.esperarTecla()
        case "4":
           opcion=False
           agenda.borra_pantalla() 
           print("Terminaste la ejecucion del SW")
        
        