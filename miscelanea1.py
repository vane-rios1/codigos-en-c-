
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Lista para almacenar el historial de alumnos
historial_alumnos = []

def mostrar_mensaje_bienvenida():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="¡Bienvenido, Vanessa Rios! ", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar Mensaje", command=lambda: messagebox.showinfo("Bienvenida", "Hola, Vanessa!!")).pack()

def mostrar_datos_alumno():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Información del Alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del Alumno:").pack()
    nombre_alumno = tk.Entry(area_dinamica)
    nombre_alumno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección de género:").pack()
    opcion_elegida = tk.StringVar(value="Masculino")
    tk.Radiobutton(area_dinamica, text="Masculino", variable=opcion_elegida, value="Masculino").pack()
    tk.Radiobutton(area_dinamica, text="Femenino", variable=opcion_elegida, value="Femenino").pack()

    tk.Label(area_dinamica, text="Calificación:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Diez", "Nueve", "Ocho"])
    combo.pack()
    combo.current(0)

    def guardar_datos():
        try:
            nombre = nombre_alumno.get()
            if not nombre:
                raise ValueError("El campo de nombre no puede estar vacío.")
            
            # Guardar los datos en la lista historial
            datos = {
                "Nombre": nombre,
                "Género": opcion_elegida.get(),
                "Calificación": combo.get()
            }
            historial_alumnos.append(datos)

            messagebox.showinfo("Revisión", f"Nombre: {nombre}\nGénero: {datos['Género']}\nCalificación: {datos['Calificación']}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos).pack(pady=10)

def mostrar_historial_alumnos():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Historial de Alumnos", font=("Arial", 14)).pack(pady=10)

    if not historial_alumnos:
        tk.Label(area_dinamica, text="No hay datos almacenados.").pack(pady=10)
    else:
        for i, alumno in enumerate(historial_alumnos, start=1):
            info = f"{i}. Nombre: {alumno['Nombre']}, Género: {alumno['Género']}, Calificación: {alumno['Calificación']}"
            tk.Label(area_dinamica, text=info, anchor="w", justify="left").pack(fill="x", padx=10)

def cambiar_tema():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Cambiar Tema", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    
    def aplicar_color(color):
        try:
            ventana_principal.config(bg=color)
            menu_lateral.config(bg=color)
            area_dinamica.config(bg=color)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cambiar el color: {e}")

    for color in colores:
        tk.Button(area_dinamica, text=color, bg=color, width=20, command=lambda col=color: aplicar_color(col)).pack(pady=2)

def mostrar_ayuda():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Preguntas", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

# Creación de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para Prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

# Creación del menú lateral
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

# Creación del área dinámica
area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

# Botones del menú lateral
tk.Button(menu_lateral, text="Inicio", command=mostrar_mensaje_bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos Alumno", command=mostrar_datos_alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Historial Alumnos", command=mostrar_historial_alumnos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cambiar Tema", command=cambiar_tema, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=mostrar_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

# Mostrar la pantalla inicial
mostrar_mensaje_bienvenida()

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()
