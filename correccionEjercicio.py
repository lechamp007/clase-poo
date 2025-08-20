import random
class CUENTA:
    def __init__(self,Titular,,NumCuenta):
        self.Titular=Titular
        self.NumCuenta=rendom.randin(10000,99999)
    def depositar(self,Cantidad):
        self.Saldo += Cantidad
        return self.Saldo
    
    def retirar(self,Retirar):
        if self.Saldo >= Retirar:
            self.Saldo = self.Saldo - Retirar
            return self.Saldo
        else:
            return -1
    def consultar(self):
        return self.Saldo


#MENÚ
NumCuenta=100
ListaClientes=[]
while True:      
    print("Bienvendido a Bancolombia")
    print("Seleccione un opción: ")
    print("1. Crear cuenta")
    print("2. Hacer un deposito")
    print("3. Hacer un retiro")
    print("4. Ver mi saldo")
    print("0. Salir")
    opcion=int(input())
    if opcion==1:
        print("Ingrese nombre del titular que estará asociada a la cuenta")
        Titular=input()
        nueva_cuenta=cuenta(nombre)
        Cliente=CUENTA(Titular,0,NumCuenta)
        ListaClientes.append(Cliente)
    elif opcion==2:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                print("Ingrese depósito:")
                Cantidad=float(input())
                print("Su Saldo actual es:", Cliente.depositar(Cantidad) )
        if InicioSesion==False:
            print("Cuenta no encontrada")

    elif opcion==3:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                print("Ingrese cuanto retirará:")
                Cantidad=float(input())
                nuevoSaldo= Cliente.retirar(Cantidad)
                if nuevoSaldo==-1:
                    print("Saldo no suficiente. Su saldo es:", Cliente.Saldo)
                else:
                    print("Su Saldo actual es:", nuevoSaldo )

        if InicioSesion==False:
            print("Cuenta no encontrada")
       
    elif opcion==4:
        print("Para iniciar sesión ingrese su número de cuenta")
        Num=int(input())
        InicioSesion=False
        for Cliente in ListaClientes:
            if Num==Cliente.NumCuenta:
                InicioSesion=True
                nuevoSaldo=Cliente.consultar()
                print("Su saldo es:", nuevoSaldo)
        if InicioSesion==False:
            print("Cuenta no encontrada")
    elif opcion==0:
        break
    else:
        print("opción incorrecta")