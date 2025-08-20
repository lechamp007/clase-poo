"""
tupla_ejemplo= (1,10,50,30)
print(tupla_ejemplo[1])

import random 
tupla2= tuple(random.randint(1,100) for i in range(5))
print (tupla2)
"""
#Ejercicios de libreria
class Libreria:
    def __init__(self, nombre):
        self.nombre= nombre 
        self.libros= []
        self.ultima_venta= None
    def agregar_libro(self,nombre_libro):
        self.libros.append(nombre_libro)
        print("Libro agregado exitosamente")
    def registrar_venta(self, cliente, total):
        self.ultima_venta= (cliente, total)
    def mostrar_libros(self):
        for i in range (0,len(self.libros)):
            print("El libro numero",i+1,"es",self.libros[i])

print("Bienvenido a la libreria de la UdeM")
librerias= []
while True: 
    print("Selecione la opción deseada")
    print("1. Crear libreria")
    print("2. Agregar un libro a la libreria ")
    print("3. Mostrar libreria")
    opcion = int(input())
    if opcion== 1:
        nombre =input("Ingrese el nombre de la libreria")
        nueva_libreria= Libreria(nombre)
        librerias.append(nueva_libreria)
    if opcion == 2: 
        nombre= input("Ingrese el nombre de la libreria").lower()# el lower me sirve para que los caracteres se pongan en minusculas
        existe= False
        for libreria in librerias:
            if libreria.nombre==nombre: 
                existe= True
                nombre_libro= input("Ingrese el nombre del libro")
                libreria.agregar_libro(nombre_libro)
        if existe == False: 
            print("No existe en la libreria")
    elif opcion== 3: 
        nombre= input("Ingrese el nombre de la libreria").lower()
        existe= False
        for libreria in librerias: 
            if libreria.nombre == nombre: 
                existe= True
                libreria.mostrar_libros()
            if existe == False: 
                print("No existe esta libreria")
    elif opcion== 4: 
        for libreria in librerias: 
            print(libreria.nombre)
            libreria.mostrar_libros()
    elif opcion== 0:
        break
    else: 
        print("Opcion incorrecta")