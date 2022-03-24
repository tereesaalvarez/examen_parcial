if __name__ == '__main__':

    from cuenta import *
    from cuentaplazofijo import *
    from cuentavip import *

    ID = 234567
    print("Su ID del banco es {}".format(ID))
    
    Titular = "Jose Alvarez"
    print("El titular de la cuenta es {}".format(Titular))
    
    numerocuenta = random.randint(100000000000, 999999999999)
    print("El numero de su cuenta es {}".format(numerocuenta))
    
    inicio = datetime(2015, 1, 30)
    final =  datetime(2019, 5, 28)
    fecha_apertura = inicio + (final - inicio) * random.random()
    print("La fecha de apertura es {}".format(fecha_apertura))

    inicio = datetime(2020, 1, 30)
    final =  datetime(2025, 5, 28)
    fecha_vencimiento = inicio + (final - inicio) * random.random()
    print("La fecha de vencimiento es {}".format(fecha_vencimiento))




    saldo = 10000
    cuentas = input("En que cuenta quiere trabajar: 1- Cuenta corriente 2- Cuenta a plazo fijo 3- Cuenta vip: ")
    operacion = input("Que operacion desea realizar: 1- Ingresar dinero 2- Retirar Dinero 3- Transferir dinero: ")

    if cuentas == 1 :
        saldo = 10000
        if operacion == 1:
            ingresar = 575
            saldo = (saldo + ingresar)
            print("Su saldo ahora es de {}".format(saldo))
        if operacion == 2:
            retirar = 78
            saldo =  (saldo - retirar)

    if cuentas == 2:
        saldo = 10000
        if operacion == 1:
            print("Ha seleccionado ingresar dinero")

        if operacion == 2:
            print("En esta cuenta al retirar dinero se le puede penalizar con un 5%")

        if operacion == 3:
            print("Ha seleccionado transferir dinero")
    



