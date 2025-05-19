
import tkinter as tk
from tkinter import messagebox

# Lista global para historial
historial_areas = []

def calcular_area():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area = (base * altura) / 2

        if area > 100:
            mensaje = f"El área del triángulo es: {area:.2f}.\nEs un área GRANDE."
        else:
            mensaje = f"El área del triángulo es: {area:.2f}.\nEs un área PEQUEÑA."

        messagebox.showinfo("Resultado", mensaje)

        # Guardar en historial
        historial_areas.append(area)
        actualizar_historial()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

def reiniciar():
    entry_base.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

def actualizar_historial():
    historial_text.config(state='normal')
    historial_text.delete("1.0", tk.END)
    for i in range(len(historial_areas)):
        area = historial_areas[i]
        historial_text.insert(tk.END, f"{i+1}. Área: {area:.2f}\n")
    historial_text.config(state='disabled')

def regresar_al_inicio():
    historial_areas.clear()
    ventana.destroy()
    main()

def salir():
    ventana.destroy()

def main():
    global ventana, entry_base, entry_altura, historial_text

# Ventana principal
    ventana = tk.Tk()
    ventana.title("Área de un Triángulo")
    ventana.geometry("360x420")
    ventana.resizable(False, False)

    # Modificación: Color de fondo personalizado
    ventana.config(bg="lightyellow")  


    # Entradas
    tk.Label(ventana, text="Base del triángulo:").pack(pady=5)
    entry_base = tk.Entry(ventana, fg="black", bg="lightpink" )
    entry_base.pack()

    tk.Label(ventana, text="Altura del triángulo:").pack(pady=5)
    entry_altura = tk.Entry(ventana, fg="black", bg="lightpink")
    entry_altura.pack()

    # Botones
    tk.Button(ventana, text="Calcular Área", command=calcular_area, fg="black", bg="lightblue").pack(pady=10)
    tk.Button(ventana, text="Reiniciar Campos", command=reiniciar, fg="black", bg="lightblue").pack(pady=5)
    tk.Button(ventana, text="Regresar al Inicio", command=regresar_al_inicio, fg="black", bg="lightblue").pack(pady=5)
    tk.Button(ventana, text="Salir", command=salir, fg="white", bg="red").pack(pady=10)

    # Historial
    tk.Label(ventana, text="Historial de áreas calculadas:").pack(pady=5)
    historial_text = tk.Text(ventana, height=6, width=40, state='disabled', bg="lightpink")
    historial_text.pack()

    ventana.mainloop()

# Iniciar la aplicación
main()