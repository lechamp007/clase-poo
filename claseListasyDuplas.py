import random
#Crear lista 
mi_lista=["primer elemento","Segundo elemento","Tercer elemento"]
longitud= len(mi_lista)
print(mi_lista[-1])

#Crear lista con ceros 
lista_ceros=[0]*10 
print(lista_ceros)

#Crear lista de aleatorios
lista_random= []
for i in range(0,11):
    lista_random.append(random.randint(1,100))
print(lista_random)

#Lista random 2 

lista_random2 = [random.randint(1,100) for _ in range (10)]

print(lista_random2)


#Remove 
lista_ejemplo = [ i for i in range (10)]
"""

lista_ejemplo[2 ]= 10 
lista_ejemplo [5] = 2
print(lista_ejemplo)

lista_ejemplo.remove(10)
print(lista_ejemplo)
#Eliminar elemento
lista_ejemplo.remove(1)
print(listra_ejemplo)

#Eliminar por posicion 
del lista_ejemplo[2]
print(lista_ejemplo)
"""
"""

#Forma de indentancion
lista_ejemplo= [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)
#Organizar datos en una lista
lista_ejemplo.reverse()#No ordena, solo voltea la lista, el ultimo de primero y asi
print(lista_ejemplo)
lista_ejemplo.sort()
print(lista_ejemplo)

lista_ejemplo.sort(reverse=True)# Ordenar de mayor a menor
print(lista_ejemplo)
"""
import random
class Persona: 
    def __init__ (self,nombre):
        self.nombre= nombre 
        self.numeros = [ random.randint(100,999) for _ in range (5)]
persona1 = Persona("Juan esteban")
persona2= Persona("Isaac")

print("Los número para", persona1.nombre, "son", persona1.numeros)
print("Los numeros para",persona2.nombre, "son ",persona2.numeros)

   




