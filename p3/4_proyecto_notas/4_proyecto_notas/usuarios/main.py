import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t ingresa tu contraseña: ").strip
            #Agregar codigo
            lista_usuario=usuario.registrar(nombre,apellidos,email,password)
            if lista_usuario:
                print(f"\n\t{nombre} {apellidos} se registro correctamente, con el email: {email}")
            else:
                print (f"\n\t No fue posible registrar el usuario intentalo mas tarde ")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t ingresa tu contraseña: ").strip
            #Agregar codigo
            lista_usuario=usuario.inicio_sesion(email,password)
            if lista_usuario:
                menu_notas(lista_usuario[0],lista_usuario[1],lista_usuario[2])
            else:
                print(f"E-mail y/o contraseña incorrectos por favor verifica y vuelve a intentar")
                funciones.esperarTecla()
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 
 
def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n\t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            resultado=nota.crear(usuario_id,titulo,descripcion)
            if resultado:
                print(f"\n\t Se creo satisfactoriamente la nota {titulo}")
            else:
                print(f"\n\t No fue posible crear la nota en este momento")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            lista_notas=nota.mostrar(usuario_id) 
            if len(lista_notas)>0:
               print(f"\n\tMostrar las Notas")
               print(f"{'ID':<10}{'Titulo':<15}{'Descripción':<20}{'Fecha':<15}")
               print(f"-"*80)
               for fila in lista_notas:
                  print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<20}   {fila[4]}")
               print(f"-"*80)
               resp=input("¿Deseas modificar alguna nota? (Si/No): ").lower().strip()
               if resp=="si":
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                    id = input("\t \t ID de la nota a actualizar: ")
                    titulo = input("\t Nuevo título: ")
                    descripcion = input("\t Nueva descripción: ")
                    #Agregar codigo
                    respuesta=nota.cambiar(id,titulo,descripcion)
                    if respuesta:
                        print(f"\n\t Se actualizo correctamente la nota {titulo}")
                    else:
                        print(f"\n\t .. No fue posible actualizar la nota es este momento intentelo de nuevo...")  
                    funciones.esperarTecla() 
            else:
                print("\n\t..No existen notas para este usuario ..")
                #agregar codigo
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            respuesta=nota.borrar(id)
            if respuesta:
                print("se borro la nota {id} correctamente ")
            else:
                    print("no es posible borrar a nota vuelve a iintetarlo mas tarde")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    

def_cambiar(id,titulo,descripcion):
   try:
    cursor.execute("updare notas set titulo=%s,descripcion%s,fecha=NOW,() where id=%s,"(titulo,descripcion,id))
    conexion.comit()
    return true
    except:
        return false 

def borrar():
    try:
        resp = input("¿Deseas borrar alguna nota? (Si/No): ").lower().strip()
        if resp == "si":
            print(f"\n \t :: {nombre} {apellidos}, vamos a borrar una Nota ::. \n")
            id_nota = input("\t\t ID de la nota a borrar: ")
            cursor.execute("DELETE FROM notas WHERE id = %s", (id_nota,))
            conexion.commit() 
            print("✅ La nota fue borrada exitosamente\n")
        else:
            print("Operación cancelada.")
    except Exception as e:
        print(f"❌ Ocurrió un error al intentar borrar la nota: {e}")
