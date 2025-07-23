from conexionBD import *

def crear(ususario_id,titulo,descripcion):
    try:
        cursor.execute("insert into notas(ususario:id,titulo,descripcion,fecha) values(%s,%s,%s,Now())",(ususario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where ususario_id=%s",(usuario_id,))
        lista=cursor.fetchall()
    except:
        return []
    