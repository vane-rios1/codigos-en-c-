
import tkinter as tk
from tkinter import messagebox

# Lista global para historial
historial_areas = []

# Ventana Principal
ventana = tk.Tk()
ventana.title("Área de un Triángulo")
ventana.geometry("360x420")
ventana.resizable(False, False)
ventana.config(bg="lightyellow")

tk.Label(ventana, text="Base del triángulo:").pack(pady=5)
entry_base = tk.Entry(ventana, fg="black", bg="lightpink")
entry_base.pack()

tk.Label(ventana, text="Altura del triángulo:").pack(pady=5)
entry_altura = tk.Entry(ventana, fg="black", bg="lightpink")
entry_altura.pack()

tk.Label(ventana, text="Historial de áreas calculadas:").pack(pady=5)
historial_text = tk.Text(ventana, height=6, width=40, state='disabled', bg="lightpink")
historial_text.pack()

# Botón Calcular Área
tk.Button(
    ventana,
    text="Calcular Área",
    fg="black",
    bg="lightblue",
    command=lambda: (
        (
            lambda base, altura: (
                messagebox.showerror("Error", "Base y altura deben ser mayores que cero.")
                if base <= 0 or altura <= 0 else (
                    historial_areas.append((base * altura) / 2),
                    messagebox.showinfo(
                        "Resultado",
                        f"Área del triángulo: {(base * altura) / 2:.2f}.\n"
                        + ("Es un área GRANDE." if (base * altura) / 2 > 100 else "Es un área PEQUEÑA.")
                    ),
                    historial_text.config(state='normal'),
                    historial_text.delete("1.0", tk.END),
                    [historial_text.insert(tk.END, f"{i+1}. Área: {a:.2f}\n") for i, a in enumerate(historial_areas)],
                    historial_text.config(state='disabled')
                )
            )
        )(
            float(entry_base.get()) if entry_base.get() else -1,
            float(entry_altura.get()) if entry_altura.get() else -1
        )
        if entry_base.get().isdigit() and entry_altura.get().isdigit()
        else messagebox.showerror("Error", "Por favor ingresa números válidos.")
    )
).pack(pady=10)

# Botón Reiniciar
tk.Button(
    ventana,
    text="Reiniciar Campos",
    fg="black",
    bg="lightblue",
    command=lambda: (
        entry_base.delete(0, tk.END),
        entry_altura.delete(0, tk.END)
    )
).pack(pady=5)





# Botón Salir
tk.Button(
    ventana,
    text="Salir",
    fg="white",
    bg="red",
    command=lambda: ventana.destroy()
).pack(pady=10)

ventana.mainloop()

