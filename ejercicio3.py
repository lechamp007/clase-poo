""" Una Tienda quiere llevar el control de los productos que vende. Por cada producto, necesita guardar
el nombre, el precio y la cantidad disponible. El sistema debe de permitir vender cierta cantidad
de productos y mostrar cuantas unidades quedan. Si no hay suficiente unidades, debe 
de mostrar un mensaje de advertencia.""" 
def producto: 
    def __init__(self,nombre, precio, cantidad):
        self.nombre= nombre
        self.precio= precio
        self.cantidad= cantidad
    def Mostrar_Datos(self)
    print("Nombre: ", self.nombre)
    print("precio: ", self.precio)
    print("Cantidad: ", self.cantidad)
    def vender: