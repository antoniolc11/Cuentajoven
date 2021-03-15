from cuenta import Cuenta
class Cuentajoven(Cuenta):
    def __init__(self, persona, cantidad, bonificacion):
        if persona.es_joven_valido():
            super().__init__(persona, cantidad)
            self.__bonificacion = bonificacion
        else:
            raise ValueError('No se puede crear la cuenta, la persona no cumple con los requisitos')

    def bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def retirar(self, persona, cantidad):
        if persona.es_joven_valido():
            return super().retirar(cantidad)
        else:
            raise ValueError('El titular no es valido')

    def mostrar(self):
        super().mostrar()
        info = 'Bonificacion: ' + self.bonificacion()
        print(info)
