if __name__ == '__main__':


    from cuenta import *
    from cuentaplazofijo import *
    from cuentavip import *

    saldo = 10000
    cuentas = input("En que cuenta quiere trabajar: 1- Cuenta corriente 2- Cuenta a plazo fijo 3- Cuenta vip: ")
    operacion = input("Que operacion desea realizar: 1- Ingresar dinero 2- Retirar Dinero 3- Transferir dinero: ")

    if cuentas == 1 :
        if operacion == 1:
            ingresar = int(input("Cual es la cantidad que desea ingresar: "))
            saldo = (saldo + ingresar).add(operacion)
            print("Su saldo ahora es de {}".format(saldo))
        if operacion == 2:
            retirar = int(input("Cual es la cantidad que desea retirar: "))
            


