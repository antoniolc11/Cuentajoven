class Cuenta:
    __numero_cuenta = 000
    def __init__(self, persona, cantidad):
        Cuenta.__numero_cuenta += 1
        self.__numero_cuenta = Cuenta.__numero_cuenta
        self.__persona = persona
        self.__cantidad = cantidad

    def numero_cuenta(self):
        return self.__numero_cuenta

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
        info_cuenta = 'Numero de cuenta: ' + str(self.numero_cuenta()) + '\n' \
                      + 'Titular: ' + self.__persona.nombre() + '\n' \
                      + 'Saldo: ' + str(self.cantidad())
        print(info_cuenta)





info = 'Numero de cuenta: ' + '1' + '\n' \
       + 'Titular: ' + 'antonio' + '\n' \
       + 'Saldo: ' + '500' + '\n'

info1 = 'Bonificacion: 10%'


linea = print('hola')
