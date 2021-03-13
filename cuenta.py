class Cuenta:
    def __init__(self, persona, cantidad):
        self.__persona = persona
        self.__cantidad = cantidad

    def persona(self):
        return self.__persona

    def cantidad(self):
        return self.__cantidad

    def set_persona(self, persona):
        self.__persona = persona

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
         if cantidad > 0:
            self.__cantidad -= cantidad

    def mostrar(self):
        return f'{self.persona()} {self.cantidad()}'
