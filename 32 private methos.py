class BaseClass:
    def __init__(self):
        self.__variable_privada = "Valor privado"

    def __metodo_privado(self):
        print("Este es un método privado")

    def metodo_publico(self):
        self.__metodo_privado()  # Llamada al método privado desde uno público


objeto_base = BaseClass()
# Esto producirá un error:
print(objeto_base.__variable_privada)
# Esto también producirá un error:
objeto_base.__metodo_privado()
