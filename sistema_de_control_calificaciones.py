import tkinter as tk
from tkinter import messagebox

# Lista global donde se almacenan los datos de alumnos y sus calificaciones
alumnos = []

# Función para agregar un alumno y su calificación a la lista
def agregar_alumno():
    nombre = entry_nombre.get().strip()  # Obtener y limpiar el nombre ingresado
    calificacion_entrada = entry_calificacion.get().strip()  # Obtener y limpiar la calificación ingresada
    # Validar que ambos campos no estén vacíos
    if not nombre or not calificacion_entrada:
        messagebox.showwarning("Advertencia", "Por favor ingresa el nombre y la calificación.")
        return
    # Intentar convertir la calificación a número decimal (float) y Mostrar error si la calificación no es un número válido
    try:
        calificacion = float(calificacion_entrada)
    except ValueError:
        messagebox.showerror("Error", "La calificación debe ser un número decimal.")
        return

    # Agregar nombre, calificación a la lista global alumnos
    alumnos.append((nombre, calificacion))
    # Limpiar las cajas de texto para nuevos datos
    entry_nombre.delete(0, tk.END)
    entry_calificacion.delete(0, tk.END)
    # Actualizar la lista visible con los datos nuevos y ordenados
    actualizar_lista()


# Función para ordenar y mostrar las calificaciones en la interfaz
def actualizar_lista():
    # Ordenar la lista alumnos por calificación de mayor a menor
    alumnos_ordenados = sorted(alumnos, key=lambda x: x[1], reverse=True)

   # Limpiar la lista visible antes de insertar los datos actualizados
    lista_resultado.delete(0, tk.END)
    # Insertar cada alumno y su calificación en la lista visible
    for nombre, calificacion in alumnos_ordenados:
        lista_resultado.insert(tk.END, f"{nombre} - {calificacion:.2f}")

    # Mostrar la calificación más alta y la más baja si hay datos
    if alumnos_ordenados:
        calif_max = alumnos_ordenados[0][1]
        calif_min = alumnos_ordenados[-1][1]
        etiqueta_max.config(text=f"Calificación más alta: {calif_max:.2f}")
        etiqueta_min.config(text=f"Calificación más baja: {calif_min:.2f}")
    else:
        # Si no hay datos, mostrar N/A
        etiqueta_max.config(text="Calificación más alta: N/A")
        etiqueta_min.config(text="Calificación más baja: N/A")

# Ventana principal
ventana = tk.Tk()
ventana.title("Control de Calificaciones")
ventana.geometry("500x400")
ventana.config(bg="lightyellow")  

# Etiqueta y campo para ingresar el nombre del alumno
tk.Label(ventana, text="Nombre del alumno:", bg="lightblue", fg="black").pack()
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack(pady=5)

# Etiqueta y campo para ingresar la calificación decimal
tk.Label(ventana, text="Calificación (decimal):", bg="lightblue", fg="black").pack()
entry_calificacion = tk.Entry(ventana, width=20)
entry_calificacion.pack(pady=5)

# Botón para agregar la calificación a la lista
btn_agregar = tk.Button(ventana, text="Agregar Calificación", command=agregar_alumno, bg="lightpink", fg="black")
btn_agregar.pack(pady=10)

# Etiqueta y lista para mostrar las calificaciones ordenadas
tk.Label(ventana, text="Lista de Calificaciones (de mayor a menor):", bg="lightblue", fg="black").pack()
lista_resultado = tk.Listbox(ventana, width=50, bg="lightpink", fg="black")
lista_resultado.pack(pady=10)

# Etiquetas para mostrar la calificación más alta y más baja
etiqueta_max = tk.Label(ventana, text="Calificación más alta: N/A", bg="lightblue", fg="black")
etiqueta_max.pack()

etiqueta_min = tk.Label(ventana, text="Calificación más baja: N/A", bg="lightblue", fg="black")
etiqueta_min.pack()

# Boton para salir del programa
btn_salir = tk.Button(ventana, text="Salir", command=ventana.quit, bg="red", fg="white")
btn_salir.pack(pady=15)

ventana.mainloop()