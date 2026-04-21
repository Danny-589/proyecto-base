import mysql.connector

print("Iniciando actualización de la base de datos...")
try:
    conexion = mysql.connector.connect(user='root', password='1234', host='127.0.0.1')
    cursor = conexion.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS rentacardas;")
    cursor.execute("USE rentacardas;")
    
    print("Eliminando tabla antigua...")
    cursor.execute("DROP TABLE IF EXISTS usuarios;")
    
    print("Creando nueva tabla de usuarios...")
    cursor.execute("""
    CREATE TABLE usuarios(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    fecha_nacimiento DATE,
    correo VARCHAR(100) UNIQUE NOT NULL,
    numero_recuperacion VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(20) DEFAULT 'admin'
    );
    """)
    
    conexion.commit()
    print("¡Tabla 'usuarios' recreada exitosamente con las nuevas columnas!")

except Exception as e:
    print(f"Error al actualizar BD: {e}")
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conexion' in locals() and conexion.is_connected(): conexion.close()
