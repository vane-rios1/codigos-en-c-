import tkinter as tk
from tkinter import messagebox

class ControlNotasGUI:
    def __init__(self, master):
        # Configuración inicial de la ventana principal
        self.master = master
        self.master.title("Control de Calificaciones")
        self.master.geometry("500x400")
        self.master.config(bg="lightyellow")

        # Lista para almacenar tuplas con (nombre, calificación)
        self.alumnos = []

        # Crear y mostrar etiquetas y campos de entrada
        tk.Label(master, text="Nombre del alumno:", bg="lightblue", fg="black").pack()
        self.entry_nombre = tk.Entry(master, width=40)
        self.entry_nombre.pack(pady=5)

        tk.Label(master, text="Calificación (decimal):", bg="lightblue", fg="black").pack()
        self.entry_calificacion = tk.Entry(master, width=20)
        self.entry_calificacion.pack(pady=5)

        # Botón para agregar calificación
        btn_agregar = tk.Button(master, text="Agregar Calificación", command=self.agregar_alumno, bg="lightpink", fg="black")
        btn_agregar.pack(pady=10)

        # Lista para mostrar resultados ordenados
        tk.Label(master, text="Lista de Calificaciones (de mayor a menor):", bg="lightblue", fg="black").pack()
        self.lista_resultado = tk.Listbox(master, width=50, bg="lightpink", fg="black")
        self.lista_resultado.pack(pady=10)

        # Etiquetas para calificación más alta y más baja
        self.etiqueta_max = tk.Label(master, text="Calificación más alta: N/A", bg="lightblue", fg="black")
        self.etiqueta_max.pack()

        self.etiqueta_min = tk.Label(master, text="Calificación más baja: N/A", bg="lightblue", fg="black")
        self.etiqueta_min.pack()

        # Botón para salir de la aplicación
        btn_salir = tk.Button(master, text="Salir", command=master.quit, bg="red", fg="white")
        btn_salir.pack(pady=15)

    def agregar_alumno(self):
        # Obtener y limpiar datos ingresados
        nombre = self.entry_nombre.get().strip()
        calificacion_entrada = self.entry_calificacion.get().strip()

        # Verificar que los campos no estén vacíos
        if not nombre or not calificacion_entrada:
            messagebox.showwarning("Advertencia", "Por favor ingresa el nombre y la calificación.")
            return

        # Verificar que la calificación sea un número decimal
        try:
            calificacion = float(calificacion_entrada)
        except ValueError:
            messagebox.showerror("Error", "La calificación debe ser un número decimal.")
            return

        # Agregar alumno a la lista
        self.alumnos.append((nombre, calificacion))

        # Limpiar los campos de entrada
        self.entry_nombre.delete(0, tk.END)
        self.entry_calificacion.delete(0, tk.END)

        # Actualizar la lista mostrada en pantalla
        self.actualizar_lista()

    def actualizar_lista(self):
        # Ordenar alumnos por calificación de mayor a menor
        alumnos_ordenados = sorted(self.alumnos, key=lambda x: x[1], reverse=True)

        # Limpiar la lista mostrada
        self.lista_resultado.delete(0, tk.END)

        # Insertar alumnos ordenados en la lista visible
        for nombre, calificacion in alumnos_ordenados:
            self.lista_resultado.insert(tk.END, f"{nombre} - {calificacion:.2f}")

        # Mostrar calificación más alta y más baja si hay datos
        if alumnos_ordenados:
            calif_max = alumnos_ordenados[0][1]
            calif_min = alumnos_ordenados[-1][1]
            self.etiqueta_max.config(text=f"Calificación más alta: {calif_max:.2f}")
            self.etiqueta_min.config(text=f"Calificación más baja: {calif_min:.2f}")
        else:
            # Si no hay datos, mostrar "N/A"
            self.etiqueta_max.config(text="Calificación más alta: N/A")
            self.etiqueta_min.config(text="Calificación más baja: N/A")

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = ControlNotasGUI(ventana)
    ventana.mainloop()