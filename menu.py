#Sistema de Alquiler de Autos
#Programador: Daniel Reátegui
#Módulo principal
#Fecha: 21/01/226
#Version: 1

import tkinter as tk #se la utiliza para crear la interfaz grafica
import customtkinter as ctk #Se la utiliza para dar un mejor diseño a la interfaz
from tkinter import PhotoImage, messagebox  #<- agraga el message box
from Cliente import agregar_cliente_db, modificar_cliente_db, eliminar_cliente_db, obtener_cliente_db
from auto import agregar_auto_db, modificar_auto_db, eliminar_auto_db, obtener_auto_db

def crear_ventana_titulo(titulo):
    ventana_aux=ctk.CTkToplevel()
    ventana_aux.title(titulo)
    ventana_aux.geometry("750x500")
    ventana_aux.grab_set()  # Evita que se pueda interactuar con la ventana principal
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
            messagebox.showinfo("Éxito", "Auto eliminado correctamente")
        else:
            messagebox.showwarning("Error", "No existe auto")


def salir():
    ventana.destroy()



#Crear ventana principal
ventana=ctk.CTk()
ventana.geometry("1200x800")
ventana.title("SISTEMA DE ALQUILER DE AUTOS")



#Incluir fondo y logo
background_image=PhotoImage(file="FOndo.png") 
#logo_image= PhotoImage(file="logotipo.png") 
background_label = tk.Label(ventana, image=background_image)
background_label.place(relwidth=1, relheight=1)
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
menu_clientes.add_command(label="Consultar", font=("arial", 10), command="consultar_cliente")
menu_principal.add_cascade(label="Clientes", menu=menu_clientes)



#Crear el menú autos
menu_autos = tk.Menu(menu_principal,tearoff=0)
menu_autos.add_command(label="Agregar", font=("arial", 10), command=agregar_autos)
menu_autos.add_command(label="Modificar", font=("arial", 10), command=modificar_autos)
menu_autos.add_command(label="Eliminar", font=("arial", 10), command=eliminar_autos)
menu_autos.add_command(label="Consultar", font=("arial", 10), command="consultar_autos")
menu_principal.add_cascade(label="Autos", menu=menu_autos)




#Crear el menú alquiler
menu_alquiler = tk.Menu(menu_principal,tearoff=0)
menu_alquiler.add_command(label="Agregar", font=("arial", 10), command="agregar_alquiler")
menu_alquiler.add_command(label="Modificar", font=("arial", 10), command="modificar_alquiler")
menu_alquiler.add_command(label="Eliminar", font=("arial", 10), command="eliminar_alquiler")
menu_alquiler.add_command(label="Consultar", font=("arial", 10), command="consultar_alquiler")
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



#Iniciar el bucle principal de la ventana
ventana.mainloop()