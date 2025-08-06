class Banco:
    def __init__(self, cuenta, titular, saldo):
        self.cuenta = cuenta
        self.titular = titular
        self.saldo = saldo
        
    def mostrar_datos(self):
        print("Cuenta: ", self.cuenta)
        print("Titular: ", self.titular)
        print("Saldo: ", self.saldo)


print("Bienvenido a NuBank")
cantidad_cuentas = []

while True:
    print("Seleccione su opción")
    print(" 1. Ingresar una nueva cuenta")
    print(" 2. Depositar")
    print(" 3. Retirar")
    print(" 4. Verificar saldo")
    print(" 0. Salir")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        titular = input("Digita el nombre del titular: ")
        cuenta = input("Digita el numero de cuenta: ")
        saldo = float(input("Saldo incial de tu cuenta: "))
        Cuentas = Banco(cuenta, titular, saldo)
        cantidad_cuentas.append(Cuentas)
        
    elif opcion == 2:
        numero = input("Por favor digite su número de cuenta: ")
        for Cuentas in cantidad_cuentas:
            if Cuentas.cuenta == numero:
                cantidad = float(input("Cantidad a depositar: "))
                Cuentas.saldo += cantidad
                print("Se ha realizado su deposito. Nuevo saldo:", Cuentas.saldo)
                
        else:
            print("Su cuenta no fue encontrada")
            
    elif opcion == 3:
        numero = input("Número de cuenta: ")
        for cuenta in cantidad_cuentas:
            if Cuentas.cuenta == numero:
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad <= cuenta.saldo:
                    Cuentas.saldo -= cantidad
                    print("Su retiro se ha realizado. Nuevo saldo:", Cuentas.saldo)
                else:
                    print("Fondos insuficientes")
                
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 4:
        numero = input("Número de cuenta: ")
        for Cuentas in cantidad_cuentas:
            if Cuentas.cuenta == numero:
                Cuentas.mostrar_datos()
               
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 0:
        print("Gracias por visitarnos")
        break