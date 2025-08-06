"""Quieres simular un sistema bancario sencillo. Cada cliente debe poder tener un número de cuenta, un titular y un saldo. 
El sistema debe permitir depositar dinero, retirar dinero (si hay suficiente), y consultar el saldo."""

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
        nueva_cuenta = Banco(cuenta, titular, saldo)
        cantidad_cuentas.append(nueva_cuenta)
        print("Cuenta creada con exito")
        
    elif opcion == 2:
        numero = input("Número de cuenta: ")
        for cuenta in cantidad_cuentas:
            if cuenta.cuenta == numero:
                cantidad = float(input("Cantidad a depositar: "))
                cuenta.saldo += cantidad
                print("Se ha realizado su deposito. Nuevo saldo:", cuenta.saldo)
                
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 3:
        numero = input("Número de cuenta: ")
        for cuenta in cantidad_cuentas:
            if cuenta.cuenta == numero:
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad <= cuenta.saldo:
                    cuenta.saldo -= cantidad
                    print("Su retiro se ha realizado. Nuevo saldo:", cuenta.saldo)
                else:
                    print("Fondos insuficientes")
                
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 4:
        numero = input("Número de cuenta: ")
        for cuenta in lista_cuenta:
            if cuenta.cuenta == numero:
                cuenta.mostrar_datos()
               
        else:
            print("Cuenta no encontrada")
            
    elif opcion == 0:
        print("Gracias por visitarnos")
        break


"""
""" Una Tienda quiere llevar el control de los productos que vende. Por cada producto, necesita guardar
el nombre, el precio y la cantidad disponible. El sistema debe de permitir vender cierta cantidad
de productos y mostrar cuantas unidades quedan. Si no hay suficiente unidades, debe 
de mostrar un mensaje de advertencia.""" 
class producto: 
    def __init__(self,nombre, precio, cantidad):
        self.nombre= nombre
        self.precio= precio
        self.cantidad= cantidad
    def Mostrar_Datos(self):
        print("Nombre: ", self.nombre)
        print("precio: ", self.precio)
        print("Cantidad: ", self.cantidad)
print("Bienvenido al sistema de Supermercados Carrulla")
lista_productos= []
while True: 
    print("Seleccione su opción")
    print("1. Agregar producto a la lista")
    print("2. Comprar producto")
    print("0. Salir")
    opcion = int(input())
#Seleccionar opcion
    if opcion==1: 
        nombre= input("Ingrese el nombre del producto: ")
        precio= float(input("ingrese el precio: "))
        cantidad= float(input("Ingrese la cantidad de productos existente: "))
        Producto= producto(nombre,precio,cantidad)
        lista_productos.append(Producto)
    if opcion == 2:
        for Producto in lista_productos:
            print(Producto.nombre, "/", Producto.precio, "/", Producto.cantidad)
        nom = input("Ingrese el nombre del producto: ")
        productoEncontrado = False
        for Producto in lista_productos:
            if Producto.nombre == nom:
                productoEncontrado = Producto
        if productoEncontrado == False:
            print("Tu Producto no esta en nuestras bases de datos")
        else:
            compra = int(input("Cuanta es la cantidad de productos que requieres: "))
            if compra > productoEncontrado.cantidad:
                print("Lo lamentamos, en este momento no contamos con esa cantidad de productos")
            else:
                productoEncontrado.cantidad -= compra
                print("Compra realizada. Quedan", productoEncontrado.cantidad, "unidades")
    if opcion== 0:
        break
    else:
        print("Opcion invalida, vuelvelo a intentar")"""