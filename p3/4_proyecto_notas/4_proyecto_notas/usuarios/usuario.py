from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def regsitrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdiges t()
        sql="insert into usuarios(nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s,)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return 
    
def inicio_sesion(email,contrasena):
    try:
        sql="select * from ususarios where email=%s and password=%s"
        val=(email,contrasena)
        cursor.exceute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None