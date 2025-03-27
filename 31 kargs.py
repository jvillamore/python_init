class Empleado:
    def __init__(self, name, *skills, **details):
        self.name = name
        self.skills = skills
        self.details = details

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Skills: {self.skills}")
        print(f"Details: {self.details}")


# Creación de un objeto e instancia de la clase
empleado = Empleado("Carlos", "Python", "Java", "C++", age=30, city="Bogotá")
empleado.show_info()


# KARGS

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Llamada a la función con diferentes argumentos
print_info(name="Carlos", age=30, city="Bogotá")


# ARGS

def sum_numbers(*args):
    return sum(args)


# Llamada a la función con diferentes números de argumentos
print(sum_numbers(1, 2, 3, 4, 5))  # Retorna 15
print(sum_numbers(1, 2))           # Retorna 3
print(sum_numbers(7, 8, 9, 10))    # Retorna 34
