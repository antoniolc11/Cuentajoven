class Persona:
    def __init__(self, nombre, edad, dni):
        if not self.dni_valido(dni):
            raise ValueError('El DNI no es valido')
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.__dni = dni

    def nombre(self):
        return self.__nombre

    def edad(self):
        return self.__edad

    def dni(self):
        return self.__dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def mostrar(self):
        return f'{self.nombre()} {self.edad()} {self.dni()}'

    def es_joven_valido(self):
        return self.edad() >= 18 and self.edad() <= 25

    def dni_valido(self, dni):
        lista = list(dni)
        num = 0
        letra = 0
        for i in lista:
            if i.isdigit():
                num += 1
            elif i.isalpha() and i == i.upper():
                letra +=1
        if num == 8 and letra == 1:
            return True
        else:
            return False
