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
def agregar_auto_db(código, matrícula, descripción, marca, tipo, modelo, color_1, color_2, nro_pasajeros, año_auto, combustible):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="insert into auto (cod_auto, mat_auto, des_auto, mar_auto, tip_auto, mod_auto, col1_auto, col2_auto, numpas_auto, a_auto, comb_auto) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(código, matrícula, descripción, marca, tipo, modelo, color_1, color_2, nro_pasajeros, año_auto, combustible))
    conexion.commit()
    cursor.close()
    conexion.close()

#Método para agregar autos desde la base de datos
def obtener_auto_db(id):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="select * from auto where id_auto=%s"
    cursor.execute(query,(id, ))
    auto=cursor.fetchone()
    cursor.close()
    conexion.close()
    return auto

#Método para modificar auto en la base de datos
def modificar_auto_db(id, código, matrícula, descripción, marca, tipo, modelo, color_1, color_2, nro_pasajeros, año_auto, combustible):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="UPDATE auto SET cod_auto=%s, mat_auto=%s , des_auto=%s , mar_auto=%s , tip_auto=%s , mod_auto=%s , col1_auto=%s , col2_auto=%s , numpas_auto=%s , a_auto=%s , comb_auto=%s WHERE id_auto=%s"
    cursor.execute(query,(código, matrícula, descripción, marca, tipo, modelo, color_1, color_2, nro_pasajeros, año_auto, combustible, id))
    conexion.commit()
    cursor.close()
    conexion.close()

    #Método para eliminar auto en la base de datos
def eliminar_auto_db(id):
    conexion=conectar_con_base_datos()
    try:
        cursor=conexion.cursor()
        query="DELETE FROM auto WHERE id_auto=%s"
        cursor.execute(query,(id, ))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El auto fue eliminado correctamente")
        else:
            print(f"No se encontro ningún auto con ese id{id}.")
    except Exception as e:
        print(f"Error al eliminar los datos:{e}")
    finally:
        cursor.close()
        conexion.close()
        

#Método para obtener todos los clientes desde la base de datos
def consultar_auto_db(id):
    conexion = conectar_con_base_datos()
    cursor = conexion.cursor()
    
    query = "SELECT * FROM auto WHERE id_auto=%s"
    cursor.execute(query,(id, ))
    
    autos = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    return autos