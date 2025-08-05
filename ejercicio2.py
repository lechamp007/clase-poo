#Crear clase estudiante
class estudiantes: 
    def __init__(self,nombre,edad,n1,n2,n3 ):
        self.nombre=nombre
        self.edad=edad
        self.n1= n1 
        self.n2 = n2
        self.n3 = n3 
    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("n1: ", self.n1)
        print("n2: ", self.n2)
        print("n3: ", self.n3)
    def  calcular_promedio(self):
        promedio= (self.n1+self.n2+self.n3/3)
        return promedio
print("Bienvenido al sistema de gestión de estuiantes")
lista_estudiantes=[]

while True: 
    print("Seleccione la opcion deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar informacion de estudiantes")
    print("3. Mostrar promedio de estudiantes ")
    print("0. Salir")
    opcion= int(input())
    if opcion== 1: 
        nombre= input("Ingrese su nombre: ")
        edad= int(input())
        print("Ingresa tu edad: ")
        n1= float(input())
        print("Ingrese la nota 1")
        n2= float(input())
        print("Ingrese la nota 2")
        n1= float(input())
        print("Ingrese la nota 3")
        persona=estudiantes
        lista_estudiantes.append(estudiante)
    if opcion== 2: 
        numero_estudiantes= len(lista_estudiantes)
        print("El numero de estudiantes es: ", numero_estudiantes)
        for estudiantes in lista_estudiantes:
            print("El nombre del estudiante es: ", estudiante.nombre())
            print("El promedio del estudiante es: ", estudiante.promedio())
    if opcion == 0:
        print("Hasta pronto")
        break 
    else: 
        print("Opcion no valida")
    

      