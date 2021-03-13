class Persona:
    def __init__(self, nombre, edad, dni):
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

    def es_mayor_edad(self):
        return self.edad() >= 18

    def es_joven_valido(self):
        if self.edad() < 25 and self.es_mayor_edad():
            return True
        else:
            return False
