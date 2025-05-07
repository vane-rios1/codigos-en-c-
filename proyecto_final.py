import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"¡Hola {nombre}, tienes {edad} años!")

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("400x200")

# Modificación: Color de fondo personalizado
ventana.config(bg="lightyellow") 

# Entrada para el nombre
etiqueta = tk.Label(ventana, text="Introduce tu nombre:", bg="orange").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Entrada para la edad
etiqueta = tk.Label(ventana, text="Introduce tu edad:", bg="lightblue").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Botón
boton_saludo = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton_saludo.pack()

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="", bg="lightpink")
etiqueta_resultado.pack()

# Modificación: Nombre del autor
etiqueta_autor = tk.Label(ventana, text="Autor: [Vanessa Rios Perez]", bg="lightgreen", font=("Arial", 8))
etiqueta_autor.pack(side="bottom")

ventana.mainloop()
