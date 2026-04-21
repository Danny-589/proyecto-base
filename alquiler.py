#Módulo para realizar Crud de clientes
#Fecha: 6/04/2026

#pip install mysql-connector-python
import mysql.connector

#Método para la conección con la base de datos

def conectar_con_base_datos():
    return mysql.connector.connect(user='root', password='1234',
                                   host='127.0.0.1',
                                   database='rentacardas',
                                   port='3306')

#Método para agragar cliente en la base de datos
def agregar_registro_db(código_alquiler, cédula_cliente, cod_auto, fecha_alquiler, observación_alquiler, estado_alquiler, kilometraje_alquiler, descuento_alquiler, valor_alquiler):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="insert into Reg_alquiler(cod_alquiler, ced_cliente, cod_auto, fec_alquiler, obs_alquiler, est_alquiler, km_alquiler, desc_alquiler, val_alquiler) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(código_alquiler, cédula_cliente, cod_auto, fecha_alquiler, observación_alquiler, estado_alquiler, kilometraje_alquiler, descuento_alquiler, valor_alquiler))
    conexion.commit()
    cursor.close()
    conexion.close()

#Método para agregar autos desde la base de datos
def obtener_registro_db(id):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="select * from Reg_alquiler where id_alquiler=%s"
    cursor.execute(query,(id, ))
    auto=cursor.fetchone()
    cursor.close()
    conexion.close()
    return auto

#Método para modificar auto en la base de datos
def modificar_registro_db(id_registro,código_alquiler, cédula_cliente, cod_auto, fecha_alquiler, observación_alquiler, estado_alquiler, kilometraje_alquiler, descuento_alquiler, valor_alquiler):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="UPDATE Reg_alquiler SET cod_alquiler=%s, ced_cliente=%s , cod_auto=%s , fec_alquiler=%s , obs_alquiler=%s , est_alquiler=%s , km_alquiler=%s , desc_alquiler=%s , val_alquiler=%s WHERE id_alquiler=%s"
    cursor.execute(query,(código_alquiler, cédula_cliente, cod_auto, fecha_alquiler, observación_alquiler, estado_alquiler, kilometraje_alquiler, descuento_alquiler, valor_alquiler, id_registro))
    conexion.commit()
    cursor.close()
    conexion.close()

    #Método para eliminar auto en la base de datos
def eliminar_registro_db(id_registro):
    conexion=conectar_con_base_datos()
    try:
        cursor=conexion.cursor()
        query="DELETE FROM Reg_alquiler WHERE id_alquiler=%s"
        cursor.execute(query,(id_registro, ))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El registro fue eliminado correctamente")
        else:
            print(f"No se encontro ningún registro con ese id{id}.")
    except Exception as e:
        print(f"Error al eliminar los datos:{e}")
    finally:
        cursor.close()
        conexion.close()


#Método para obtener todos los clientes desde la base de datos
def consultar_registro_db(id):
    conexion = conectar_con_base_datos()
    cursor = conexion.cursor()
    
    query = "SELECT * FROM Reg_alquiler WHERE id_alquiler=%s"
    cursor.execute(query,(id, ))
    
    alquiler = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    return alquiler
        