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
def agregar_cliente_db(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="insert into cliente (ced_cliente ,nom_cliente ,ape_cliente , sex_cliente , dir_cliente , tel_cliente , cor_cliente,fec_nac_cliente) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac))
    conexion.commit()
    cursor.close()
    conexion.close()

#Método para agregar clientes desde la base de datos
def obtener_cliente_db(id):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="select * from cliente where id_cliente=%s"
    cursor.execute(query,(id, ))
    cliente=cursor.fetchone()
    cursor.close()
    conexion.close()
    return cliente

#Método para modificar cliente en la base de datos
def modificar_cliente_db(id, cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac):
    conexion=conectar_con_base_datos()
    cursor=conexion.cursor()
    query="UPDATE cliente SET ced_cliente=%s, nom_cliente=%s ,ape_cliente=%s , sex_cliente=%s , dir_cliente=%s , tel_cliente=%s , cor_cliente=%s, fec_nac_cliente=%s WHERE id_cliente=%s"
    cursor.execute(query,(cedula, nombres, apellidos, sexo, direccion, telefono, correo, fecha_nac, id))
    conexion.commit()
    cursor.close()
    conexion.close()

    #Método para eliminar cliente en la base de datos
def eliminar_cliente_db(id):
    conexion=conectar_con_base_datos()
    try:
        cursor=conexion.cursor()
        query="DELETE FROM cliente WHERE id_cliente=%s"
        cursor.execute(query,(id, ))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El cliente fue eliminado correctamente")
        else:
            print(f"No se encontro ningún cliente con ese id{id}.")
    except Exception as e:
        print(f"Error al eliminar los datos:{e}")
    finally:
        cursor.close()
        conexion.close()

#Método para obtener todos los clientes desde la base de datos
def consultar_cliente_db(id):
    conexion = conectar_con_base_datos()
    cursor = conexion.cursor()
    
    query = "SELECT * FROM cliente WHERE id_cliente=%s"
    cursor.execute(query,(id, ))
    
    clientes = cursor.fetchone()
    
    cursor.close()
    conexion.close()
    
    return clientes