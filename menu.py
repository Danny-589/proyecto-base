#Sistema de Alquiler de Autos
#Programador: Daniel Reátegui
#Módulo principal
#Fecha: 21/01/226
#Version: 1

import tkinter as tk #se la utiliza para crear la interfaz grafica
import customtkinter as ctk #Se la utiliza para dar un mejor diseño a la interfaz
from tkinter import PhotoImage, messagebox  #<- agraga el message box
from Cliente import agregar_cliente_db, modificar_cliente_db, eliminar_cliente_db, obtener_cliente_db, consultar_cliente_db
from auto import agregar_auto_db, modificar_auto_db, eliminar_auto_db, obtener_auto_db, consultar_auto_db
from alquiler import agregar_registro_db, modificar_registro_db, eliminar_registro_db, obtener_registro_db, consultar_registro_db
from usuario import agregar_usuario_db, verificar_usuario_db
import math
from PIL import Image, ImageTk, ImageFilter

class AnimatedBackground(tk.Canvas):
    def __init__(self, parent, image_path, *args, **kwargs):
        super().__init__(parent, highlightthickness=0, *args, **kwargs)
        self.image_path = image_path
        self.angle = 0
        self.bg_img = None
        self.img_item = None
        try:
            # Difuminar la imagen estáticamente para no consumir CPU y aplicar resize responsivo
            self.pil_img_orig = Image.open(image_path).filter(ImageFilter.GaussianBlur(30))
        except Exception as e:
            print("Error cargando fondo:", e)
            self.pil_img_orig = None
        
        self.bind("<Configure>", self.on_resize)
        self.animate()

    def on_resize(self, event):
        if not self.pil_img_orig: return
        self.width = event.width
        self.height = event.height
        if self.width <= 1 or self.height <= 1: return
        
        # Redimensionado dinámico a las medidas de ventana, manteniendo margen para paneo
        pil_img = self.pil_img_orig.resize((int(self.width * 1.5), int(self.height * 1.5)), Image.Resampling.NEAREST)
        self.bg_img = ImageTk.PhotoImage(pil_img)
        
        if self.img_item is None:
            self.img_item = self.create_image(0, 0, image=self.bg_img, anchor="center")
        else:
            self.itemconfig(self.img_item, image=self.bg_img)

    def animate(self):
        try:
            if hasattr(self, 'width') and self.img_item is not None:
                # Rotación en órbita escalada
                radius = min(self.width, self.height) * 0.1
                x = (self.width / 2) + radius * math.cos(self.angle)
                y = (self.height / 2) + radius * math.sin(self.angle)
                self.coords(self.img_item, x, y)
                self.angle += 0.05
                if self.angle >= math.pi * 2:
                    self.angle = 0
            self.after(16, self.animate) # 60 FPS fluido
        except:
            pass  # Widget fue destruido

def crear_ventana_titulo(titulo):
    ventana_aux=ctk.CTkToplevel(ventana)  # Ahora se asigna la ventana principal como "padre"
    ventana_aux.title(titulo)
    ventana_aux.geometry("750x500")
    
    ventana_aux.transient(ventana) # Asegura que NUNCA se oculte detrás de la ventana principal
    ventana_aux.lift()
    ventana_aux.focus_force()
    ventana_aux.grab_set() # Para asegurar enfoque al presionar
    
    # Aparece al frente como Registro, pero permite otras apps encima en Windows
    ventana_aux.attributes("-topmost", True)
    ventana_aux.after(50, lambda: ventana_aux.attributes("-topmost", False)) 

    ventana_aux.configure(bg="lightblue")
    ventana_aux.resizable(True, True)
    return ventana_aux




#Método para crear la interfaz para agragar clientes
def agregar_cliente():
    ventana_agregar=crear_ventana_titulo("Agregar Cliente")

    contenedor=ctk.CTkFrame(ventana_agregar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Cédula:").grid(row=0, column=0, padx=10, pady=10)
    entry_cedula=ctk.CTkEntry(contenedor)
    entry_cedula.grid(row=0, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Nombres:").grid(row=0, column=2, padx=10, pady=10)
    entry_nombres=ctk.CTkEntry(contenedor)
    entry_nombres.grid(row=0, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Apellidos:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellidos=ctk.CTkEntry(contenedor)
    entry_apellidos.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Sexo:").grid(row=1, column=2, padx=10, pady=10)
    entry_sexo=ctk.CTkEntry(contenedor)
    entry_sexo.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Dirección:").grid(row=2, column=0, padx=10, pady=10)
    entry_direccion=ctk.CTkEntry(contenedor)
    entry_direccion.grid(row=2, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Teléfono:").grid(row=2, column=2, padx=10, pady=10)
    entry_telefono=ctk.CTkEntry(contenedor)
    entry_telefono.grid(row=2, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Correo:").grid(row=3, column=0, padx=10, pady=10)
    entry_correo=ctk.CTkEntry(contenedor)
    entry_correo.grid(row=3, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Fecha de nacimiento:").grid(row=3, column=2, padx=10, pady=10)
    entry_fecha_nac=ctk.CTkEntry(contenedor)
    entry_fecha_nac.grid(row=3, column=3, padx=10, pady=10)
    
    ctk.CTkButton(contenedor, text="Guardar", command=lambda:
    guardar_datos("Agregar", 
                  entry_cedula.get(),
                  entry_nombres.get(),
                  entry_apellidos.get(),
                  entry_sexo.get(),
                  entry_direccion.get(),
                  entry_telefono.get(),
                  entry_correo.get(),
                  entry_fecha_nac.get())).grid(
                      row=4, column=0, columnspan=4, pady=10)




#Método para crear la interfaz para modificar clientes
def modificar_cliente():
    ventana_modificar=crear_ventana_titulo("Modificar Cliente")

    contenedor=ctk.CTkFrame(ventana_modificar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Id del cliente:").grid(row=0, column=0, padx=10, pady=10)
    entry_id=ctk.CTkEntry(contenedor)
    entry_id.grid(row=0, column=1, padx=80, pady=10)
    
    ctk.CTkLabel(contenedor, text="Cédula:").grid(row=0, column=2, padx=10, pady=10)
    entry_cedula=ctk.CTkEntry(contenedor)
    entry_cedula.grid(row=0, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Nombres:").grid(row=1, column=0, padx=10, pady=10)
    entry_nombres=ctk.CTkEntry(contenedor)
    entry_nombres.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Apellidos:").grid(row=1, column=2, padx=10, pady=10)
    entry_apellidos=ctk.CTkEntry(contenedor)
    entry_apellidos.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Sexo:").grid(row=2, column=0, padx=10, pady=10)
    entry_sexo=ctk.CTkEntry(contenedor)
    entry_sexo.grid(row=2, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Dirección:").grid(row=2, column=2, padx=10, pady=10)
    entry_direccion=ctk.CTkEntry(contenedor)
    entry_direccion.grid(row=2, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
    entry_telefono=ctk.CTkEntry(contenedor)
    entry_telefono.grid(row=3, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Correo:").grid(row=3, column=2, padx=10, pady=10)
    entry_correo=ctk.CTkEntry(contenedor)
    entry_correo.grid(row=3, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Fecha de nacimiento:").grid(row=4, column=0, padx=10, pady=10)
    entry_fecha_nac=ctk.CTkEntry(contenedor)
    entry_fecha_nac.grid(row=4, column=1, padx=80, pady=10)
    
    ctk.CTkButton(contenedor, text="Guardar", command=lambda:
    guardar_datos("Modificar",
                  entry_cedula.get(),
                  entry_nombres.get(),
                  entry_apellidos.get(),
                  entry_sexo.get(),
                  entry_direccion.get(),
                  entry_telefono.get(),
                  entry_correo.get(),
                  entry_fecha_nac.get(),
                  entry_id.get()
                  )).grid(row=5, column=0, columnspan=4, pady=10)




#Método para Cargar datos del cliente
    def cargar_dato_cliente():
        id_cliente=entry_id.get()
        if id_cliente:
            cliente=obtener_cliente_db(id_cliente)
            if cliente:
                entry_cedula.delete(0,tk.END)
                entry_cedula.insert(0,cliente[1])
                
                entry_nombres.delete(0,tk.END)
                entry_nombres.insert(0,cliente[2])

                entry_apellidos.delete(0,tk.END)
                entry_apellidos.insert(0,cliente[3])
                
                entry_sexo.delete(0,tk.END)
                entry_sexo.insert(0,cliente[4])
                
                entry_direccion.delete(0,tk.END)
                entry_direccion.insert(0,cliente[5])
                
                entry_telefono.delete(0,tk.END)
                entry_telefono.insert(0,cliente[6])
                
                entry_correo.delete(0,tk.END)
                entry_correo.insert(0,cliente[7])
                
                entry_fecha_nac.delete(0,tk.END)
                entry_fecha_nac.insert(0,cliente[8])

            else:
                messagebox.showerror("Error", "Cliente no encontrado")
        
        else:
            messagebox.showwarning("Atención", "Ingrese un ID")

#Botón Buscar
    ctk.CTkButton(contenedor, text="Buscar", command=cargar_dato_cliente).grid(row=6, column=0, columnspan=4, pady=5)
            



#Método para crear la interfaz para eliminar clientes
def eliminar_cliente():
    ventana_agregar=crear_ventana_titulo("Eliminar Cliente")

    contenedor=ctk.CTkFrame(ventana_agregar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)

    ctk.CTkLabel(contenedor, text="Id del cliente que desea borrar:").grid(row=0, column=0, padx=10, pady=5)
    
    entry_id=ctk.CTkEntry(contenedor)
    entry_id.grid(row=0, column=1, padx=10, pady=5)
    ctk.CTkButton(contenedor, text="Confirmar", command=lambda:
    eliminar_datos("Eliminar", entry_id.get())).grid(row=1, column=0, columnspan=2, pady=10)

def consultar_cliente():
    ventana_consultar = crear_ventana_titulo("Consultar Cliente")

    contenedor = ctk.CTkFrame(ventana_consultar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    ctk.CTkLabel(contenedor, text="Ingrese ID del cliente:").grid(row=0, column=0, padx=10, pady=10)

    entry_id = ctk.CTkEntry(contenedor)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    resultado = ctk.CTkLabel(contenedor, text="")
    resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def buscar():
        id_cliente = entry_id.get()
        if id_cliente:
            cliente = consultar_cliente_db(id_cliente)
            if cliente:
                resultado.configure(
                    text=f"Cédula: {cliente[1]}\nNombre: {cliente[2]} {cliente[3]}"
                )
            else:
                    resultado.configure(text="Cliente no encontrado")
        else:
            resultado.configure(text="Ingrese un ID")

    ctk.CTkButton(contenedor, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2, pady=10)


def guardar_datos(accion, 
                  cedula=None, 
                  nombres=None, 
                  apellidos=None, 
                  sexo=None, 
                  direccion=None, 
                  telefono=None, 
                  correo=None, 
                  fecha_nac=None, 
                  id=None):
    if accion=="Agregar":
        if cedula and nombres and apellidos and sexo and direccion and telefono and correo and fecha_nac:
            agregar_cliente_db(cedula, 
                               nombres, 
                               apellidos, 
                               sexo, 
                               direccion, 
                               telefono, 
                               correo, 
                               fecha_nac)
            messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        else:
            messagebox.showwarning("Error", "Faltan datos para modigicar cliente")

    elif accion=="Modificar":   
        if cedula and nombres and apellidos and sexo and direccion and telefono and correo and fecha_nac and id:
            modificar_cliente_db(cedula, 
                                 nombres, 
                                 apellidos, 
                                 sexo, 
                                 direccion, 
                                 telefono, 
                                 correo, 
                                 fecha_nac, 
                                 id)
            messagebox.showinfo("Éxito", "Cliente modificado correctamente")



def eliminar_datos(accion, id=None):
    if accion=="Eliminar":
        if id:
            eliminar_cliente_db(id)
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
        else:
            messagebox.showwarning("Error", "No existe cliente")

























































#Método para crear la interfaz para agragar autos
def agregar_autos():
    ventana_agregar_auto=crear_ventana_titulo("Agregar Auto")

    contenedor=ctk.CTkFrame(ventana_agregar_auto)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Código:").grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_código=ctk.CTkEntry(contenedor)
    entry_código.grid(row=0, column=1, padx=5, pady=10, sticky="ew")


    ctk.CTkLabel(contenedor, text="Matrícula:").grid(row=0, column=2, padx=(50, 10), pady=10, sticky="e")
    
    entry_matrícula=ctk.CTkEntry(contenedor)
    entry_matrícula.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Descripción:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_descripción=ctk.CTkEntry(contenedor)
    entry_descripción.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Marca:").grid(row=1, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_marca=ctk.CTkEntry(contenedor)
    entry_marca.grid(row=1, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Tipo:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_tipo=ctk.CTkEntry(contenedor)
    entry_tipo.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Modelo:").grid(row=2, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_modelo=ctk.CTkEntry(contenedor)
    entry_modelo.grid(row=2, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Color 1:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_color_1=ctk.CTkEntry(contenedor)
    entry_color_1.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Color 2:").grid(row=3, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_color_2=ctk.CTkEntry(contenedor)
    entry_color_2.grid(row=3, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Número de pasajeros:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_nro_pasajeros=ctk.CTkEntry(contenedor)
    entry_nro_pasajeros.grid(row=4, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Año de fabricación:").grid(row=4, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_año_auto=ctk.CTkEntry(contenedor)
    entry_año_auto.grid(row=4, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Tipo de combustible:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
    entry_combustible=ctk.CTkEntry(contenedor)
    entry_combustible.grid(row=5, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkButton(
        contenedor, text="Guardar", command=lambda:
        guardar_datos_auto(
            "Agregar", 
            entry_código.get(),
            entry_matrícula.get(), 
            entry_descripción.get(),
            entry_marca.get(),
            entry_tipo.get(), 
            entry_modelo.get(),
            entry_color_1.get(),
            entry_color_2.get(),
            entry_nro_pasajeros.get(), 
            entry_año_auto.get(), 
            entry_combustible.get()
        )
    ).grid(row=6, column=0, columnspan=4, pady=10)




#Método para crear la interfaz para modificar autos
def modificar_autos():
    ventana_modificar_auto=crear_ventana_titulo("Modificar Auto")

    contenedor=ctk.CTkFrame(ventana_modificar_auto)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)    
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Id del Auto:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_auto=ctk.CTkEntry(contenedor)
    entry_id_auto.grid(row=0, column=1, padx=80, pady=10)
    
    ctk.CTkLabel(contenedor, text="Código:").grid(row=0, column=2, padx=10, pady=10)
    entry_código=ctk.CTkEntry(contenedor)
    entry_código.grid(row=0, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Matrícula:").grid(row=1, column=0, padx=10, pady=10)
    entry_matrícula=ctk.CTkEntry(contenedor)
    entry_matrícula.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Descripción:").grid(row=1, column=2, padx=10, pady=10)
    entry_descripción=ctk.CTkEntry(contenedor)
    entry_descripción.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Marca:").grid(row=2, column=0, padx=10, pady=10)
    entry_marca=ctk.CTkEntry(contenedor)
    entry_marca.grid(row=2, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Tipo:").grid(row=2, column=2, padx=10, pady=10)
    entry_tipo=ctk.CTkEntry(contenedor)
    entry_tipo.grid(row=2, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Modelo:").grid(row=3, column=0, padx=10, pady=10)
    entry_modelo=ctk.CTkEntry(contenedor)
    entry_modelo.grid(row=3, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Color 1:").grid(row=3, column=2, padx=10, pady=10)
    entry_color_1=ctk.CTkEntry(contenedor)
    entry_color_1.grid(row=3, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Color 2:").grid(row=4, column=0, padx=10, pady=10)
    entry_color_2=ctk.CTkEntry(contenedor)
    entry_color_2.grid(row=4, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Número de pasajeros:").grid(row=4, column=2, padx=10, pady=10)
    entry_nro_pasajeros=ctk.CTkEntry(contenedor)
    entry_nro_pasajeros.grid(row=4, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Año de fabricación:").grid(row=5, column=0, padx=10, pady=10)
    entry_año_auto=ctk.CTkEntry(contenedor)
    entry_año_auto.grid(row=5, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Tipo de combustible:").grid(row=5, column=2, padx=10, pady=10)
    entry_combustible=ctk.CTkEntry(contenedor)
    entry_combustible.grid(row=5, column=3, padx=10, pady=10)
    
    ctk.CTkButton(contenedor, text="Guardar", command=lambda:
    guardar_datos_auto("Modificar", 
                       entry_id_auto.get(),
                       entry_código.get(),
                       entry_matrícula.get(),
                       entry_descripción.get(),
                       entry_marca.get(),
                       entry_tipo.get(),
                       entry_modelo.get(),
                       entry_color_1.get(),
                       entry_color_2.get(),
                       entry_nro_pasajeros.get(),
                       entry_año_auto.get(),
                       entry_combustible.get())).grid(
                           row=6, column=0, columnspan=4, pady=10)




#Método para Cargar datos del Auto
    def cargar_dato_auto():
        id_auto=entry_id_auto.get()
        if id_auto:
            auto=obtener_auto_db(id_auto)
            if auto:
                entry_código.delete(0,tk.END)
                entry_código.insert(0,auto[1])
                
                entry_matrícula.delete(0,tk.END)
                entry_matrícula.insert(0,auto[2])

                entry_descripción.delete(0,tk.END)
                entry_descripción.insert(0,auto[3])
                
                entry_marca.delete(0,tk.END)
                entry_marca.insert(0,auto[4])
                
                entry_tipo.delete(0,tk.END)
                entry_tipo.insert(0,auto[5])
                
                entry_modelo.delete(0,tk.END)
                entry_modelo.insert(0,auto[6])
                
                entry_color_1.delete(0,tk.END)
                entry_color_1.insert(0,auto[7])
                
                entry_color_2.delete(0,tk.END)
                entry_color_2.insert(0,auto[8])
                
                entry_nro_pasajeros.delete(0,tk.END)
                entry_nro_pasajeros.insert(0,auto[9])
                
                entry_año_auto.delete(0,tk.END)
                entry_año_auto.insert(0,auto[10])
                
                entry_combustible.delete(0,tk.END)
                entry_combustible.insert(0,auto[11])

            else:
                messagebox.showerror("Error", "Auto no encontrado")
        
        else:
            messagebox.showwarning("Atención", "Ingrese el Id del auto")



#Botón Buscar
    ctk.CTkButton(contenedor, text="Buscar", command=cargar_dato_auto).grid(row=7, column=0, columnspan=4, pady=10)
            




#Método para crear la interfaz para eliminar autos
def eliminar_autos():
    ventana_agregar_auto=crear_ventana_titulo("Eliminar Auto")

    contenedor=ctk.CTkFrame(ventana_agregar_auto)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)

    ctk.CTkLabel(contenedor, text="Id del auto que desea borrar:").grid(row=0, column=0, padx=10, pady=10)
    
    entry_id_auto=ctk.CTkEntry(contenedor)
    entry_id_auto.grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkButton(contenedor, text="Confirmar", command=lambda:
    eliminar_datos_auto("Eliminar", entry_id_auto.get())).grid(row=2, column=0, columnspan=2, pady=10)


def consultar_autos():
    ventana_consultar = crear_ventana_titulo("Consultar Auto")

    contenedor = ctk.CTkFrame(ventana_consultar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    ctk.CTkLabel(contenedor, text="Ingrese ID del auto:").grid(row=0, column=0, padx=10, pady=10)

    entry_id_auto = ctk.CTkEntry(contenedor)
    entry_id_auto.grid(row=0, column=1, padx=10, pady=10)

    resultado = ctk.CTkLabel(contenedor, text="")
    resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def buscar():
        id_auto = entry_id_auto.get()
        if id_auto:
            auto = consultar_auto_db(id_auto)
            if auto:
                resultado.configure(
                    text=f"Cédula: {auto[1]}\nNombre: {auto[2]} {auto[3]}"
                )
            else:
                    resultado.configure(text="Cliente no encontrado")
        else:
            resultado.configure(text="Ingrese un ID")

    ctk.CTkButton(contenedor, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2, pady=10)



def guardar_datos_auto(accion, código=None, matrícula=None, descripción=None, marca=None, tipo=None, modelo=None, color_1=None, color_2=None, nro_pasajeros=None, año_auto=None, combustible=None, id_auto=None):
    if accion=="Agregar":
        if código and matrícula and descripción and marca and tipo and modelo and color_1 and color_2 and nro_pasajeros and año_auto and combustible:
            agregar_auto_db(código, 
                            matrícula, 
                            descripción,
                            marca, 
                            tipo, 
                            modelo, 
                            color_1, 
                            color_2, 
                            nro_pasajeros, 
                            año_auto, 
                            combustible)
            messagebox.showinfo("Éxito", "Auto agregado correctamente")
        else:
            messagebox.showwarning("Error", "Faltan datos para modigicar los datos del auto")

    elif accion=="Modificar":   
        if código and matrícula and descripción and marca and tipo and modelo and color_1 and color_2 and nro_pasajeros and año_auto and combustible and id_auto:
            modificar_auto_db(código, 
                              matrícula, 
                              descripción, 
                              marca, 
                              tipo, 
                              modelo, 
                              color_1, 
                              color_2, 
                              nro_pasajeros, 
                              año_auto, 
                              combustible, 
                              id_auto)
            messagebox.showinfo("Éxito", "Auto modificado correctamente")




def eliminar_datos_auto(accion, id_auto=None):
    if accion=="Eliminar":
        if id_auto:
            eliminar_auto_db(id_auto)
            messagebox.showinfo("Éxito", "Registro eliminado correctamente")
        else:
            messagebox.showwarning("Error", "No existe auto")
























































#Método para crear la interfaz para agragar autos
def agregar_registro():
    ventana_agregar_reg=crear_ventana_titulo("Agregar Registro de Alquiler")

    contenedor=ctk.CTkFrame(ventana_agregar_reg)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Código de Alquiler:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_código_alquiler=ctk.CTkEntry(contenedor)
    entry_código_alquiler.grid(row=0, column=1, padx=5, pady=10, sticky="ew")


    ctk.CTkLabel(contenedor, text="Cédula del Cliente:").grid(row=0, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_cédula_cliente=ctk.CTkEntry(contenedor)
    entry_cédula_cliente.grid(row=0, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Código del Auto:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_código_auto=ctk.CTkEntry(contenedor)
    entry_código_auto.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Fecha de Alquiler:").grid(row=1, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_fecha_alquiler=ctk.CTkEntry(contenedor)
    entry_fecha_alquiler.grid(row=1, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Observaciones del Alquiler:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_observaciones_alquiler=ctk.CTkEntry(contenedor)
    entry_observaciones_alquiler.grid(row=2, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Estado de alquiler:").grid(row=2, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_estado_alquiler=ctk.CTkEntry(contenedor)
    entry_estado_alquiler.grid(row=2, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Kilometraje de alquiler:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_kilometraje_alquiler=ctk.CTkEntry(contenedor)
    entry_kilometraje_alquiler.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Descripción del alquiler:").grid(row=3, column=2, padx=(50, 10), pady=10, sticky="e")
    entry_descripción_alquiler=ctk.CTkEntry(contenedor)
    entry_descripción_alquiler.grid(row=3, column=3, padx=5, pady=10, sticky="ew")

    ctk.CTkLabel(contenedor, text="Valor del alquiler:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
    entry_valor_alquiler=ctk.CTkEntry(contenedor)
    entry_valor_alquiler.grid(row=4, column=1, padx=5, pady=10, sticky="ew")

    ctk.CTkButton(
        contenedor, text="Guardar", command=lambda:
        guardar_datos_reg(
            "Agregar", 
            entry_código_alquiler.get(),
            entry_cédula_cliente.get(),
            entry_código_auto.get(),
            entry_fecha_alquiler.get(),
            entry_observaciones_alquiler.get(),
            entry_estado_alquiler.get(),
            entry_kilometraje_alquiler.get(),
            entry_descripción_alquiler.get(),
            entry_valor_alquiler.get()
        )
    ).grid(row=6, column=0, columnspan=4, pady=10)


#Método para crear la interfaz para registrar alquileres
def modificar_registro():
    ventana_modificar_registro=crear_ventana_titulo("Modificar Registro de Alquiler")

    contenedor=ctk.CTkFrame(ventana_modificar_registro)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)    
    contenedor.grid_columnconfigure(2, weight=1)
    contenedor.grid_columnconfigure(3, weight=2)

    ctk.CTkLabel(contenedor, text="Id del alquiler:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_alquiler=ctk.CTkEntry(contenedor)
    entry_id_alquiler.grid(row=0, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Código del alquiler:").grid(row=0, column=2, padx=10, pady=10)
    entry_código_alquiler=ctk.CTkEntry(contenedor)
    entry_código_alquiler.grid(row=0, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Cédula del cliente:").grid(row=1, column=0, padx=10, pady=10)
    entry_cédula_cliente=ctk.CTkEntry(contenedor)
    entry_cédula_cliente.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Código del auto:").grid(row=1, column=2, padx=10, pady=10)
    entry_código_auto=ctk.CTkEntry(contenedor)
    entry_código_auto.grid(row=1, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Fecha de alquiler:").grid(row=1, column=0, padx=10, pady=10)
    entry_fecha_alquiler=ctk.CTkEntry(contenedor)
    entry_fecha_alquiler.grid(row=1, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Observaciones del alquiler:").grid(row=2, column=0, padx=10, pady=10)
    entry_observaciones_alquiler=ctk.CTkEntry(contenedor)
    entry_observaciones_alquiler.grid(row=2, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Estado del alquiler:").grid(row=2, column=2, padx=10, pady=10)
    entry_estado_alquiler=ctk.CTkEntry(contenedor)
    entry_estado_alquiler.grid(row=2, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Kilometraje del alquiler:").grid(row=3, column=0, padx=10, pady=10)
    entry_kilometraje_alquiler=ctk.CTkEntry(contenedor)
    entry_kilometraje_alquiler.grid(row=3, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Descripción del alquiler:").grid(row=3, column=2, padx=10, pady=10)
    entry_descripción_alquiler=ctk.CTkEntry(contenedor)
    entry_descripción_alquiler.grid(row=3, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Valor del alquiler:").grid(row=4, column=0, padx=10, pady=10)
    entry_valor_alquiler=ctk.CTkEntry(contenedor)
    entry_valor_alquiler.grid(row=4, column=1, padx=80, pady=10)

    ctk.CTkLabel(contenedor, text="Número de pasajeros:").grid(row=4, column=2, padx=10, pady=10)
    entry_nro_pasajeros=ctk.CTkEntry(contenedor)
    entry_nro_pasajeros.grid(row=4, column=3, padx=10, pady=10)

    ctk.CTkLabel(contenedor, text="Año de fabricación:").grid(row=5, column=0, padx=10, pady=10)
    entry_año_auto=ctk.CTkEntry(contenedor)
    entry_año_auto.grid(row=5, column=1, padx=80, pady=10)

    
    ctk.CTkButton(
        contenedor, text="Guardar", command=lambda:
        guardar_datos_reg(
            "Modificar",
            entry_id_alquiler.get(),
            entry_código_auto.get(),
            entry_cédula_cliente.get(),
            entry_código_auto.get(),
            entry_fecha_alquiler.get(),
            entry_observaciones_alquiler.get(),
            entry_estado_alquiler.get(),
            entry_kilometraje_alquiler.get(),
            entry_descripción_alquiler.get(),
            entry_valor_alquiler.get(),
        )
    ).grid(row=6, column=0, columnspan=4, pady=10)




#Método para Cargar datos del Auto
    def cargar_dato_reg():
        id_alquiler=entry_id_alquiler.get()
        if id_alquiler:
            registro=obtener_registro_db(id_alquiler)
            if registro:
                entry_id_alquiler.delete(0,tk.END)
                entry_id_alquiler.insert(0,registro[0])

                entry_código_alquiler.delete(0,tk.END)
                entry_código_alquiler.insert(0,registro[1])

                entry_cédula_cliente.delete(0,tk.END)
                entry_cédula_cliente.insert(0,registro[2])

                entry_código_auto.delete(0,tk.END)
                entry_código_auto.insert(0,registro[3])

                entry_fecha_alquiler.delete(0,tk.END)
                entry_fecha_alquiler.insert(0,registro[4])
                
                entry_observaciones_alquiler.delete(0,tk.END)
                entry_observaciones_alquiler.insert(0,registro[5])
                
                entry_estado_alquiler.delete(0,tk.END)
                entry_estado_alquiler.insert(0,registro[6])
                
                entry_kilometraje_alquiler.delete(0,tk.END)
                entry_kilometraje_alquiler.insert(0,registro[7])
                
                entry_descripción_alquiler.delete(0,tk.END)
                entry_descripción_alquiler.insert(0,registro[8])
                
                entry_valor_alquiler.delete(0,tk.END)
                entry_valor_alquiler.insert(0,registro[9])

            else:
                messagebox.showerror("Error", "Auto no encontrado")
        
        else:
            messagebox.showwarning("Atención", "Ingrese el Id del auto")



#Botón Buscar
    ctk.CTkButton(contenedor, text="Buscar", command=cargar_dato_reg).grid(row=7, column=0, columnspan=4, pady=10)
            




#Método para crear la interfaz para eliminar autos
def eliminar_registro():
    ventana_agregar_auto=crear_ventana_titulo("Eliminar Auto")

    contenedor=ctk.CTkFrame(ventana_agregar_auto)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    contenedor.grid_columnconfigure(0, weight=1)
    contenedor.grid_columnconfigure(1, weight=2)

    ctk.CTkLabel(contenedor, text="Id del auto que desea borrar:").grid(row=0, column=0, padx=10, pady=10)
    
    entry_id_auto=ctk.CTkEntry(contenedor)
    entry_id_auto.grid(row=1, column=0, padx=10, pady=10)
    ctk.CTkButton(contenedor, text="Confirmar", command=lambda:
    eliminar_datos_alquiler("Eliminar", entry_id_auto.get())).grid(row=2, column=0, columnspan=2, pady=10)

def consultar_registro():
    ventana_consultar = crear_ventana_titulo("Consultar Registro de Alquiler")

    contenedor = ctk.CTkFrame(ventana_consultar)
    contenedor.pack(expand=True, fill="both", padx=100, pady=20)

    ctk.CTkLabel(contenedor, text="Ingrese ID del registro:").grid(row=0, column=0, padx=10, pady=10)

    entry_id_alquiler = ctk.CTkEntry(contenedor)
    entry_id_alquiler.grid(row=0, column=1, padx=10, pady=10)

    resultado = ctk.CTkLabel(contenedor, text="")
    resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def buscar():
        id_alquiler = entry_id_alquiler.get()
        if id_alquiler:
            reg = consultar_registro_db(id_alquiler)
            if reg:
                resultado.configure(
                    text=f"Cédula: {reg[1]}\nNombre: {reg[2]} {reg[3]}"
                )
            else:
                    resultado.configure(text="Cliente no encontrado")
        else:
            resultado.configure(text="Ingrese un ID")

    ctk.CTkButton(contenedor, text="Buscar", command=buscar).grid(row=2, column=0, columnspan=2, pady=10)



def guardar_datos_reg(accion, código_alquiler=None, cédula_cliente=None, código_auto=None, fecha_alquiler=None, observaciones_alquiler=None, estado_alquiler=None, kilometraje_alquiler=None, descripción_alquiler=None, valor_alquiler=None, id_alquiler=None):
    if accion=="Agregar":
        if código_alquiler and cédula_cliente and código_auto and fecha_alquiler and observaciones_alquiler and estado_alquiler and kilometraje_alquiler and descripción_alquiler and valor_alquiler:
            agregar_registro_db(código_alquiler, 
                            cédula_cliente, 
                            código_auto, 
                            fecha_alquiler, 
                            observaciones_alquiler, 
                            estado_alquiler, 
                            kilometraje_alquiler, 
                            descripción_alquiler, 
                            valor_alquiler)
            messagebox.showinfo("Éxito", "Registro de alquiler agregado correctamente")
        else:
            messagebox.showwarning("Error", "Faltan datos para agregar al registro")

    elif accion=="Modificar":   
        if código_alquiler and cédula_cliente and código_auto and fecha_alquiler and observaciones_alquiler and estado_alquiler and kilometraje_alquiler and descripción_alquiler and valor_alquiler and id_alquiler:
            modificar_registro_db(código_alquiler, 
                              cédula_cliente, 
                              código_auto, 
                              fecha_alquiler, 
                              observaciones_alquiler, 
                              estado_alquiler, 
                              kilometraje_alquiler, 
                              descripción_alquiler, 
                              valor_alquiler, 
                              id_alquiler)
            messagebox.showinfo("Éxito", "Registro modificado correctamente")


def eliminar_datos_alquiler(accion, id_alquiler=None):
    if accion=="Eliminar":
        if id_alquiler:
            eliminar_registro_db(id_alquiler)
            messagebox.showinfo("Éxito", "Registro eliminado correctamente")
        else:
            messagebox.showwarning("Error", "No existe auto registrado a nombre de ningun cliente")



























































def salir():
    ventana.destroy()

def iniciar_sesion(usuario, password, window):
    # Uso de la base de datos real
    if verificar_usuario_db(usuario, password):
        messagebox.showinfo("Éxito", "Bienvenido Administrador/Dueño al Sistema")
        window.withdraw()  # Se oculta en vez de destruir para evitar errores de Tcl del hilo 'after'
        ventana.deiconify()  # Muestra la ventana principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.\nSolo administradores autorizados.")

def draw_login_ui(login_window):
    for widget in login_window.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            widget.destroy()

    login_window.title("Login")

    contenedor = ctk.CTkFrame(login_window, fg_color="#0A1931", corner_radius=15, border_width=1, border_color="#1E3A8A")
    
    login_window.update_idletasks()
    current_width = login_window.winfo_width()
    max_ancho = 600
    if current_width > max_ancho:
        initial_pad = 50 + (current_width - max_ancho) // 2
    else:
        initial_pad = 50
    contenedor.pack(expand=True, fill="both", padx=initial_pad, pady=50)

    def limitar_ancho_login(event):
        if event.widget == login_window:
            max_ancho = 600  # Permite que el contenedor alcance 600px de ancho
            if event.width > max_ancho:
                nuevo_pad = 50 + (event.width - max_ancho) // 2
                contenedor.pack_configure(padx=nuevo_pad)
            else:
                contenedor.pack_configure(padx=50)

    login_window.bind("<Configure>", limitar_ancho_login)

    ctk.CTkLabel(contenedor, text="Welcome Back", font=("Arial", 28, "bold"), text_color="white").pack(pady=(20, 10))
    ctk.CTkLabel(contenedor, text="Panel Exclusivo para Administradores", font=("Arial", 12), text_color="#94A3B8").pack(pady=(0, 20))

    entry_user = ctk.CTkEntry(contenedor, placeholder_text="Usuario / Correo", height=40, border_width=1, border_color="#1E3A8A", fg_color="#050C1A", text_color="white", placeholder_text_color="gray")
    entry_user.pack(fill="x", padx=30, pady=10)

    entry_pass = ctk.CTkEntry(contenedor, placeholder_text="Contraseña", show="*", height=40, border_width=1, border_color="#1E3A8A", fg_color="#050C1A", text_color="white", placeholder_text_color="gray")
    entry_pass.pack(fill="x", padx=30, pady=10)

    ctk.CTkButton(contenedor, text="Log In", height=30, fg_color="#F97316", hover_color="#EA580C", font=("Arial", 16, "bold"), text_color="white", command=lambda: iniciar_sesion(entry_user.get(), entry_pass.get(), login_window)).pack(fill="x", padx=30, pady=25)
    
    ctk.CTkLabel(contenedor, text="¿Eres nuevo dueño/administrador?", text_color="gray").pack(pady=5)
    ctk.CTkButton(contenedor, text="Crear Cuenta", height=30, fg_color="transparent", border_width=1, border_color="#1E3A8A", text_color="white", hover_color="#1E40AF", command=lambda: draw_register_ui(login_window)).pack(pady=5)


def draw_register_ui(login_window):
    for widget in login_window.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            widget.destroy()

    login_window.title("Register")

    contenedor = ctk.CTkFrame(login_window, fg_color="#0A1931", corner_radius=15, border_width=1, border_color="#1E3A8A")
    
    login_window.update_idletasks()
    current_width = login_window.winfo_width()
    max_ancho = 600
    if current_width > max_ancho:
        initial_pad = 40 + (current_width - max_ancho) // 2
    else:
        initial_pad = 40
    contenedor.pack(expand=True, fill="both", padx=initial_pad, pady=30)

    def limitar_ancho_reg(event):
        if event.widget == login_window:
            max_ancho = 600  # Permite que las entradas alcancen máximo 600px
            if event.width > max_ancho:
                nuevo_pad = 40 + (event.width - max_ancho) // 2
                contenedor.pack_configure(padx=nuevo_pad)
            else:
                contenedor.pack_configure(padx=40)
                
    login_window.bind("<Configure>", limitar_ancho_reg)

    ctk.CTkLabel(contenedor, text="Register", font=("Arial", 28, "bold"), text_color="white").pack(pady=(20, 25))

    def create_theme_entry(container, placeholder, is_password=False):
        e = ctk.CTkEntry(
            container, 
            placeholder_text=placeholder, 
            height=40, 
            border_width=1, 
            border_color="#1E3A8A", 
            fg_color="#050C1A",
            text_color="white",
            placeholder_text_color="gray",
            show="*" if is_password else ""
        )
        e.pack(fill="x", padx=30, pady=8)
        return e

    entry_nombres = create_theme_entry(contenedor, "Nombres")
    entry_apellidos = create_theme_entry(contenedor, "Apellidos")
    entry_usuario = create_theme_entry(contenedor, "Usuario")
    entry_fecha = create_theme_entry(contenedor, "Fecha de Nacimiento (AAAA-MM-DD)")
    entry_correo = create_theme_entry(contenedor, "Correo Electrónico")
    entry_recuperacion = create_theme_entry(contenedor, "Núm. Recuperación")
    entry_pass = create_theme_entry(contenedor, "Contraseña", is_password=True)
    entry_pass_conf = create_theme_entry(contenedor, "Confirmar Contraseña", is_password=True)

    def registrar():
        nombres = entry_nombres.get()
        apellidos = entry_apellidos.get()
        usuario = entry_usuario.get()
        fecha_nac = entry_fecha.get()
        correo = entry_correo.get()
        num_reco = entry_recuperacion.get()
        password = entry_pass.get()
        pass_conf = entry_pass_conf.get()

        if nombres and apellidos and usuario and fecha_nac and correo and num_reco and password and pass_conf:
            if password != pass_conf:
                messagebox.showerror("Error", "Las contraseñas no coinciden.")
                return

            exito = agregar_usuario_db(nombres, apellidos, usuario, fecha_nac, correo, num_reco, password)
            if exito:
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.\nIniciando sesión del administrador automáticamente...")
                login_window.withdraw()
                ventana.deiconify()
            else:
                messagebox.showerror("Error", "No se pudo registrar. Es posible que el correo o usuario ya estén en uso.")
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")

    btn_registrar = ctk.CTkButton(
        contenedor, 
        text="Create Account", 
        height=30,
        fg_color="#F97316",
        hover_color="#EA580C",
        font=("Arial", 16, "bold"),
        text_color="white",
        command=registrar
    )
    btn_registrar.pack(fill="x", padx=30, pady=(20, 10))

    btn_cancel = ctk.CTkButton(
        contenedor,
        text="Cancel",
        height=30,
        fg_color="#1E3A8A",
        hover_color="#1E40AF",
        text_color="white",
        command=lambda: draw_login_ui(login_window)
    )
    btn_cancel.pack(fill="x", padx=30, pady=5)


def mostrar_login():
    login_window = ctk.CTkToplevel()
    login_window.geometry("500x700")  # Tamaño base para que quepan ambos formularios
    
    login_window.lift()
    login_window.attributes("-topmost", True)
    login_window.after(10, lambda: login_window.attributes("-topmost", False))
    
    login_window.protocol("WM_DELETE_WINDOW", salir)

    # Animated Background Layer responsivo
    bg = AnimatedBackground(login_window, "assets/fluid_bg.png")
    bg.place(x=0, y=0, relwidth=1, relheight=1)

    draw_login_ui(login_window)



#Crear ventana principal
ventana=ctk.CTk()
ventana.geometry("1200x800")
ventana.title("SISTEMA DE ALQUILER DE AUTOS")
ventana.withdraw() # Ocultamos la ventana principal hasta iniciar sesión



#Incluir fondo y logo con viñeta difuminada
background_image=PhotoImage(file="FOndo_dark.png") 
background_label = tk.Label(ventana, image=background_image)
background_label.place(relwidth=1, relheight=1)

#logo_image= PhotoImage(file="logotipo.png") 
#logo_label = tk.Label(ventana, image=logo_image, bg="lightblue")
#logo_label.place(x=10, y=10)



#Crear el menú principal
menu_principal = tk.Menu(ventana)
ventana.configure(menu=menu_principal)



#Crear el menú clientes
menu_clientes = tk.Menu(menu_principal,tearoff=0)
menu_clientes.add_command(label="Agregar", font=("arial", 10), command=agregar_cliente)
menu_clientes.add_command(label="Modificar", font=("arial", 10), command=modificar_cliente)
menu_clientes.add_command(label="Eliminar", font=("arial", 10), command=eliminar_cliente)
menu_clientes.add_command(label="Consultar", font=("arial", 10), command=consultar_cliente)
menu_principal.add_cascade(label="Clientes", menu=menu_clientes)



#Crear el menú autos
menu_autos = tk.Menu(menu_principal,tearoff=0)
menu_autos.add_command(label="Agregar", font=("arial", 10), command=agregar_autos)
menu_autos.add_command(label="Modificar", font=("arial", 10), command=modificar_autos)
menu_autos.add_command(label="Eliminar", font=("arial", 10), command=eliminar_autos)
menu_autos.add_command(label="Consultar", font=("arial", 10), command=consultar_autos)
menu_principal.add_cascade(label="Autos", menu=menu_autos)




#Crear el menú alquiler
menu_alquiler = tk.Menu(menu_principal,tearoff=0)
menu_alquiler.add_command(label="Agregar", font=("arial", 10), command=agregar_registro)
menu_alquiler.add_command(label="Modificar", font=("arial", 10), command=modificar_registro)
menu_alquiler.add_command(label="Eliminar", font=("arial", 10), command=eliminar_registro)
menu_alquiler.add_command(label="Consultar", font=("arial", 10), command=consultar_registro)
menu_principal.add_cascade(label="Alquiler", menu=menu_alquiler)




#Crear el menú ayuda
menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_ayuda.add_command(label="Documentación", font=("arial", 10), command="agregar_ayuda")
menu_ayuda.add_command(label="Tutorial", font=("arial", 10), command="modificar_ayuda")
menu_ayuda.add_command(label="Licencia", font=("arial", 10), command="eliminar_ayuda")
menu_ayuda.add_command(label="Guía Online", font=("arial", 10), command="consultar_ayuda")
menu_ayuda.add_command(label="Registro de Usuarios", font=("arial", 10), command="consultar_ayuda")
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)






#Crear la opción salir en el menú
menu_principal.add_command(label="salir",command=salir)
ventana.configure(menu=menu_principal)



# Mostrar Login Antes de Iniciar
mostrar_login()

#Iniciar el bucle principal de la ventana
ventana.mainloop()