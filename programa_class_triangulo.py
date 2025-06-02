class Triangulo:
    def _init_(self):
        # Ya definido: atributos base y altura
        self.base = 0
        self.altura = 0

    # Aquí va la funcion "leer_datos()"
    def leer_datos(self):
        # Solicita al usuario que ingrese la base y la convierte a float
        self.base = float(input("Ingresa la base del triángulo: "))
        # Solicita al usuario que ingrese la altura y la convierte a float
        self.altura = float(input("Ingresa la altura del triángulo: "))

    # Aquí va la funcion "calcular_area()"
    def calcular_area(self):
        # Calcula y retorna el área del triángulo
        return (self.base * self.altura) / 2

# Aquí va el código principal
t = Triangulo()          # Crea un objeto llamado "t" a partir de la "clase Triangulo"
t.leer_datos()           # Llama al método "leer_datos" con ese objeto
print("El área del triángulo es:", t.calcular_area())  # Imprime el resultado de "calcular_area()"