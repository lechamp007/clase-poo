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
    def vender(self, cantidad_a_vender):
        if self.cantidad>= cantidad_a_vender:
        self.cantidad= self.cantidad- cantidad_a_vender
        print("Producto vendido correctamente")
    else:
        print("No hay cantidad disponible de este producto")
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
        print("Opcion invalida, vuelvelo a intentar")