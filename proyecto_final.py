import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"¡Hola {nombre}, tienes {edad} años!")

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("400x200")

# Entrada para el nombre
etiqueta = tk.Label(ventana, text="Introduce tu nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Entrada para la edad
etiqueta = tk.Label(ventana, text="Introduce tu edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Botón
boton_saludo = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton_saludo.pack()

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()
