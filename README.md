# 🚗 Sistema de Gestión de Autos

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-red.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/UI-Tkinter-yellow.svg)](https://docs.python.org/3/library/tkinter.html)

Plataforma integral para la gestión de autos, clientes y registros (historial de mantenimiento). Incluye API en Python (Flask), Interfaz de Escritorio (para administración y control), y un portal Web básico para clientes.

---

## 📌 1. Requerimientos del Sistema

### 🔹 Requerimientos Funcionales
**1. Gestión de Autos:**
*   Registrar nuevos autos en el inventario.
*   Editar la información existente del auto.
*   Eliminar autos del sistema.
*   Listar todos los autos registrados.
*   Buscar autos por: placa, modelo, o nombre del propietario.

**2. Gestión de Clientes:**
*   Registrar información de clientes.
*   Editar datos de clientes.
*   Eliminar registros de clientes.
*   Listar todos los clientes.

**3. Gestión de Registros (Historial):**
*   Registrar eventos u operaciones por vehículo (mantenimiento, ingreso, reparaciones, etc.).
*   Consultar historial completo por vehículo.
*   Filtrar registros específicos por fecha.

**4. Panel de Autorización y Usuarios:**
*   Login seguro para administradores y operadores (Autenticación JWT o sesiones protegidas).
*   Control de acceso basado en roles para manejar la información del sistema.

**5. Página Web (Portal Clientes):**
*   Interfaz web pública para consultar un vehículo ingresando número de cédula del dueño y/o placa.
*   Visualización de los datos básicos del auto asociado junto con su historial completo cronológico.

### 🔹 Requerimientos No Funcionales
*   **Base de datos:** MySQL.
*   **Backend / API:** Python (Flask o FastAPI).
*   **Interfaz de Escritorio:** Tkinter / CustomTkinter para ofrecer un panel de gestión nativo a los operarios.
*   **Web (Frontend):** HTML, CSS moderno, JS nativo integrando la API del backend.
*   **Seguridad:** Hashing seguro para contraseñas usando `bcrypt`, validación sanitizada de datos, y uso de tokens JWT si se implementa una autenticación REST.
*   **Calidad de Código:** Modular, aplicando principios de separación de UI con SQL/Lógica pura (MVC/Capas).

---

## 📌 2. Diseño de Base de Datos (MySQL)

El motor principal es MySQL. Esta es la estructura y script de creación sugeridos:

```sql
CREATE DATABASE sistema_autos;
USE sistema_autos;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE autos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(20) UNIQUE NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    anio INT,
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

CREATE TABLE registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    auto_id INT,
    descripcion TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (auto_id) REFERENCES autos(id) ON DELETE CASCADE
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL -- Guardado de claves cifradas
);
```

---

## 📌 3. Backend en Python (Flask API)

Para gestionar los datos y separar la lógica, construimos una API capaz de contestar peticiones en formatos JSON para cualquier cliente (sea web o escritorio).

```python
from flask import Flask, request, jsonify
from flask_cors import CORS # Necesario para llamados web
import mysql.connector

app = Flask(__name__)
CORS(app) # Habilitar CORS para consultas desde el entorno Web

def conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_autos"
    )

# Obtener autos por cédula de cliente
@app.route("/api/autos/cliente/<cedula>", methods=["GET"])
def obtener_autos(cedula):
    try:
        db = conexion()
        cursor = db.cursor(dictionary=True)
        query = """
        SELECT autos.* FROM autos
        JOIN clientes ON autos.cliente_id = clientes.id
        WHERE clientes.cedula = %s
        """
        cursor.execute(query, (cedula,))
        data = cursor.fetchall()
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()

# Obtener Historial por placa del vehículo
@app.route("/api/historial/<placa>", methods=["GET"])
def historial(placa):
    try:
        db = conexion()
        cursor = db.cursor(dictionary=True)
        query = """
        SELECT registros.* FROM registros
        JOIN autos ON registros.auto_id = autos.id
        WHERE autos.placa = %s
        """
        cursor.execute(query, (placa,))
        data = cursor.fetchall()
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```
*(Nota: Un entorno de producción requerirá validación de token y manejo integral avanzado de errores).*

---

## 📌 4. Interfaz de Escritorio (Escalable a CustomTkinter)

El Front end de operación interna estará en Tkinter o CustomTkinter, separando la lógica SQL.

```python
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Lo ideal es conectar el front de escritorio a los endpoints en el Backend Flask
# Por arquitectura básica aquí mostramos conexión a BD directa por ahora.

def conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_autos"
    )

def registrar_cliente():
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    
    if not nombre or not cedula:
        messagebox.showwarning("Atención", "Debe llenar todos los campos")
        return

    db = conexion()
    cursor = db.cursor()

    try:
        cursor.execute("INSERT INTO clientes(nombre, cedula) VALUES(%s,%s)", (nombre, cedula))
        db.commit()
        messagebox.showinfo("Éxito", "Cliente registrado exitosamente")
        entry_nombre.delete(0, 'end')
        entry_cedula.delete(0, 'end')
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo registrar: {err}")
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()

# Generación UI básica
ventana = tk.Tk()
ventana.title("Admin Panel - Sistema de Autos")
ventana.geometry("300x250")

tk.Label(ventana, text="Nombre Cliente").pack(pady=(10, 0))
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Cédula Perteneciente").pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack(pady=5)

tk.Button(ventana, text="Registrar Cliente", command=registrar_cliente, bg="#0052cc", fg="white").pack(pady=10)

ventana.mainloop()
```

---

## 📌 5. Página Web (Portal para Clientes)

Permite visualizar el estatus del auto e historial, conectándose estrictamente a la API Backend.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Vehículos y Servicios</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input, button { padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc; width: 100%; box-sizing: border-box; }
        button { background-color: #28a745; color: white; border: none; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #218838; }
        ul { list-style-type: none; padding: 0; }
        li { background: #e9ecef; margin-top: 5px; padding: 10px; border-left: 5px solid #007bff; border-radius: 4px; }
    </style>
</head>
<body>

<div class="container">
    <h2>Consulta Estado del Vehículo</h2>
    <p>Ingrese su número de cédula para ver sus autos registrados.</p>
    <input type="text" id="cedula" placeholder="Ej: 110293021">
    <button onclick="buscar()">Buscar Autos</button>

    <ul id="resultado"></ul>
</div>

<script>
async function buscar() {
    let cedula = document.getElementById("cedula").value;
    if (!cedula) return alert("Ingrese una cédula de búsqueda");

    try {
        let res = await fetch(`http://localhost:5000/api/autos/cliente/${cedula}`);
        let responseJson = await res.json();
        
        let lista = document.getElementById("resultado");
        lista.innerHTML = "";

        if(responseJson.status === "success" && responseJson.data.length > 0) {
            responseJson.data.forEach(auto => {
                let li = document.createElement("li");
                li.innerHTML = `<strong>Auto Encontrado:</strong> Placa: <em>${auto.placa}</em> <br> <strong>Modelo/Marca:</strong> ${auto.modelo} - ${auto.marca}`;
                lista.appendChild(li);
            });
        } else {
            lista.innerHTML = "<li>No se encontraron vehículos o cliente con esa información.</li>";
        }
    } catch (error) {
        console.error("Fallo de conexión al Backend:", error);
        alert("El Backend no responde o está apagado");
    }
}
</script>

</body>
</html>
```

---

## 📌 6. Estructura y Arquitectura del Proyecto

Usa la siguiente estructura propuesta como patrón estándar para crecimiento:

```text
sistema_autos/
│
├── backend/                  # Servidor y lógicas de peticiones REST
│   ├── app.py                # Entrada de la API Flask
│   ├── requirements.txt      # Paquetes y dependencias core de Python
│   └── models/               # Archivos para interactuar con la Base de datos (Pydantic/Clases Python)
│
├── desktop/                  # Aplicación de escritorio / Administrador Local
│   ├── main.py               # Ejecución de UI Tkinter
│   ├── screens/              # Diferentes ventanas modulares del aplicativo
│   └── assets/               # Logos, Íconos, etc.
│
├── web/                      # FrontEnd accesible a Clientes externos
│   ├── index.html            # Portal principal
│   ├── css/                  # Archivos directos de cascada
│   └── js/                   # Archivos integrados de funciones javascript
│
└── database/
    ├── schema.sql            # Script de setup de la BD MySQL
    └── seeds.sql             # (Opcional) Datos prueba para inserción masiva.
```

---

## 📌 7. Instalación y Uso

**Requisitos previstos para trabajar:**
*   Instalar [Python 3.10+](https://www.python.org/downloads/)
*   Instalar e inicializar el entorno [MySQL](https://www.mysql.com/downloads/) (XAMPP o Workbench funcionan correctamente).

### Setup Paso a Paso
1. **Configurar la Base de Datos:**
   Importa o ejecuta el código dentro de `database/schema.sql` en tu entorno (PHPMyAdmin o línea de comandos MySQL).
2. **Dependencias de Backend:**
   Inicia virtualenv en la terminal y realiza:
   ```bash
   pip install flask flask-cors mysql-connector-python bcrypt
   ```
3. **Poner el backend a correr:**
   ```bash
   cd backend
   python app.py
   # Debería mostrar "Running on http://127.0.0.1:5000"
   ```
4. **Ver Interfaz Escritorio / Administrador:**
   ```bash
   cd desktop
   python main.py
   ```
5. **Ver Interfaz Web Cliente:**
   Simplemente da doble clic en `web/index.html` con un navegador o abre con _Live Server_ desde VS Code.

---

## 🔥 8. Roadmap & Subidas de Nivel

Este proyecto es la base perfecta para ir evolucionando. Como pasos de mejoras (Nivel PRO):

*   **API REST completa (CRUD):** Desarrollar controladores con métodos `POST`, `PUT`, y `DELETE` estandarizados en base a principios REST.
*   **Autenticación con tokens (JWT):** Implementar Flask-JWT-Extended para no dar acceso directo a operaciones sin Headers de autorización válidos.
*   **Seguridad y bcrypt:** Las tablas de base de datos como las passwords de administradores se protegerán con un Hash irrepetible de Bcrypt en cada POST de creacion de usuario.
*   **ORM en el DB:** Usa *SQLAlchemy* en vez de sentencias SQL planas en el backend Python. Proveerá seguridad nativa de inyección SQL y facilidad en las uniones.
*   **Web Avanzado y Despliegue Público (React & Vercel):** Transicionar la UI de web del HTML/JS simple hacia React.js (o Next.js) y desplegar en Vercel unido con base de datos en cloud (ejemplo, Neon/PostgreSQL).
*   **Panel admin web:** Para universalizar la administración, toda la gestión Desktop puede ser transformada en un dashboard administrativo web (React Admin, o similar).