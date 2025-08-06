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
    print("3. Cantidad de unidades")
    opcion = int(input())
#Seleccionar opcion
    if opcion==1: 
        nombre= input("Ingrese el nombre del producto: ")
        precio= float(input("ingrese el precio: "))
        cantidad= float(input("Ingrese la cantidad de productos existente: "))
        Producto= producto(nombre,precio,cantidad)
        lista_productos.append(Producto)
    if opcion== 2: 
        nombre producto=len(lista_productos)
        for Producto in lista_productos:
            print(Producto.nombre,"/",Producto.precio"/" Producto.cantidad)
        print("Ingrese el nombre del producto")
        nom=int()
        productoEncontrado=False
        for Producto in lista_productos:
            if Producto.nombre== nom:
                productoEncontrado=Producto
        if productoEncontrado== False: 
            print("Tu Producto no esta en nuestras bases de datos")   
        else: 
            Compra=int(input("Cuanta es la cantidad de productos que requieres: "))
            if compra>prroductoEncontrado.cantidad:
                print("Lo lamentamos, en este momento no contamos con esa cantidad de productos")
            else: 
                productoEncontrado -= compra 
    opcion == 3: 
    for producto in lista_productos:
        print("Nombre: ", producto.nombre)
        print("Cantidad disponible: ", producto)
        pritn("\*")

    if opcion== 0: 
        print("Gracias por su visita, hasta pronto")
        break
    else:
        print("Opcion invalida, vuelvelo a intentar")