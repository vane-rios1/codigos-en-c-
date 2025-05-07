import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola {nombre}!")

# Ventana principal
ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x150")

# Entada nombre
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

# Botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Etiqueta de resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()