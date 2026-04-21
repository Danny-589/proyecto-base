#Módulo para realizar control de usuarios / inicio de sesión
#Fecha: 20/04/2026

import mysql.connector

#Método para la conexión con la base de datos
def conectar_con_base_datos():
    return mysql.connector.connect(user='root', password='1234',
                                   host='127.0.0.1',
                                   database='rentacardas',
                                   port='3306')

#Método para agregar usuario administrador a la base de datos
def agregar_usuario_db(nombres, apellidos, usuario, fecha_nacimiento, correo, numero_recuperacion, password):
    conexion = conectar_con_base_datos()
    cursor = conexion.cursor()
    query = "INSERT INTO usuarios (nombres, apellidos, usuario, fecha_nacimiento, correo, numero_recuperacion, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (nombres, apellidos, usuario, fecha_nacimiento, correo, numero_recuperacion, password))
        conexion.commit()
        exito = True
    except mysql.connector.Error as err:
        print(f"Error al registrar: {err}")
        exito = False
    finally:
        cursor.close()
        conexion.close()
    return exito

#Método para verificar si el usuario y contraseña son correctos
def verificar_usuario_db(usuario_o_correo, password):
    conexion = conectar_con_base_datos()
    cursor = conexion.cursor()
    query = "SELECT * FROM usuarios WHERE (usuario=%s OR correo=%s) AND password=%s"
    cursor.execute(query, (usuario_o_correo, usuario_o_correo, password))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario is not None
