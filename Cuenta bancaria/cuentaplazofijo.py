import random
from datetime import datetime
class cuentaplazofijo:
    def __init__(self,cuenta, dinero, saldo, operacion):
        self.cuenta = cuenta
        self.dinero = dinero
        self.saldo = saldo
        self.operacion = operacion
       
    def retirar_saldo(self,retirar, saldo, saldo_nuevo):
        
        retirar = int(input("Escriba la cantidad que desea retirar"))
        saldo_nuevo = saldo - retirar
        print(saldo_nuevo)

    def ingresar(self, ingresar):
        ingresar = 575

    def get_rnd_date(start, end, fmt):

        s = datetime.strptime(start, fmt)
        e = datetime.strptime(end, fmt)

        delta = e - s

        return s + datetime(days=(random.random() * delta.days))

        get_rnd_date("01/01/2017", "01/02/2017", "%d/%m/%Y")