class cuenta:
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

