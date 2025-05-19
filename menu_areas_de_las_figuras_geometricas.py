
import tkinter as tk
from tkinter import messagebox
import math

# Historial general
historial = []

def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

def pantalla_inicio():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="¡Bienvenido/a!", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(area_dinamica, text="Hola, esta aplicación te permite calcular el área de diferentes figuras geométricas.", font=("Arial", 12), wraplength=400).pack(pady=10)

def pantalla_triangulo():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Área de un Triángulo", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(area_dinamica, text="Fórmula: (base × altura) / 2", font=("Arial", 12)).pack(pady=5)

    tk.Label(area_dinamica, text="Base:").pack()
    entrada_base = tk.Entry(area_dinamica)
    entrada_base.pack()

    tk.Label(area_dinamica, text="Altura:").pack()
    entrada_altura = tk.Entry(area_dinamica)
    entrada_altura.pack()

    def calcular():
        try:
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            area = (base * altura) / 2
            resultado = f"Triángulo: base={base}, altura={altura} → área={area}"
            historial.append(resultado)
            messagebox.showinfo("Resultado", resultado)
        except:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    tk.Button(area_dinamica, text="Calcular área", command=calcular).pack(pady=10)

def pantalla_cuadrado():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Área de un Cuadrado", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(area_dinamica, text="Fórmula: lado × lado", font=("Arial", 12)).pack(pady=5)

    tk.Label(area_dinamica, text="Lado:").pack()
    entrada_lado = tk.Entry(area_dinamica)
    entrada_lado.pack()

    def calcular():
        try:
            lado = float(entrada_lado.get())
            area = lado ** 2
            resultado = f"Cuadrado: lado={lado} → área={area}"
            historial.append(resultado)
            messagebox.showinfo("Resultado", resultado)
        except:
            messagebox.showerror("Error", "Por favor, ingresa un valor válido.")

    tk.Button(area_dinamica, text="Calcular área", command=calcular).pack(pady=10)

def pantalla_circulo():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Área de un Círculo", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(area_dinamica, text="Fórmula: π × radio²", font=("Arial", 12)).pack(pady=5)

    tk.Label(area_dinamica, text="Radio:").pack()
    entrada_radio = tk.Entry(area_dinamica)
    entrada_radio.pack()

    def calcular():
        try:
            radio = float(entrada_radio.get())
            area = math.pi * radio ** 2
            resultado = f"Círculo: radio={radio} → área={area:.2f}"
            historial.append(resultado)
            messagebox.showinfo("Resultado", resultado)
        except:
            messagebox.showerror("Error", "Por favor, ingresa un valor válido.")

    tk.Button(area_dinamica, text="Calcular área", command=calcular).pack(pady=10)

def pantalla_rectangulo():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Área de un Rectángulo", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(area_dinamica, text="Fórmula: base × altura", font=("Arial", 12)).pack(pady=5)

    tk.Label(area_dinamica, text="Base:").pack()
    entrada_base = tk.Entry(area_dinamica)
    entrada_base.pack()

    tk.Label(area_dinamica, text="Altura:").pack()
    entrada_altura = tk.Entry(area_dinamica)
    entrada_altura.pack()

    def calcular():
        try:
            base = float(entrada_base.get())
            altura = float(entrada_altura.get())
            area = base * altura
            resultado = f"Rectángulo: base={base}, altura={altura} → área={area}"
            historial.append(resultado)
            messagebox.showinfo("Resultado", resultado)
        except:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

    tk.Button(area_dinamica, text="Calcular área", command=calcular).pack(pady=10)

def pantalla_historial():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Historial de Cálculos", font=("Arial", 14, "bold")).pack(pady=10)

    if historial:
        for i, item in enumerate(historial, 1):
            tk.Label(area_dinamica, text=f"{i}. {item}", anchor="w", justify="left").pack()
    else:
        tk.Label(area_dinamica, text="No se ha realizado ningún cálculo aún.").pack()

# --- Interfaz principal ---
ventana = tk.Tk()
ventana.title("Calculadora de Áreas")
ventana.geometry("600x500")
ventana.config(bg="lightblue")

menu = tk.Frame(ventana, bg="lightblue", width=150)
menu.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

# Botones del menú
tk.Button(menu, text="Inicio", command=pantalla_inicio, width=18).pack(pady=5)
tk.Button(menu, text="Triángulo", command=pantalla_triangulo, width=18).pack(pady=5)
tk.Button(menu, text="Cuadrado", command=pantalla_cuadrado, width=18).pack(pady=5)
tk.Button(menu, text="Círculo", command=pantalla_circulo, width=18).pack(pady=5)
tk.Button(menu, text="Rectángulo", command=pantalla_rectangulo, width=18).pack(pady=5)
tk.Button(menu, text="Historial", command=pantalla_historial, width=18).pack(pady=20)
tk.Button(menu, text="Salir", command=ventana.destroy, width=18).pack(pady=30)

pantalla_inicio()
ventana.mainloop()