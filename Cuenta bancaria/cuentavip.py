class cuentavip():
    def __init__(self):
        self.name = 'cuentavip'

    def negativo(self,saldo):
        saldo = 10000
        saldo_negativo = int(input("Cual quiere que sea su saldo negativo"))
        if saldo < saldo_negativo:
            print