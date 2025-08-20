"""
#Crear la agenda 
agenda = {
    "Ana":"202020",
    "Bruno" "12211",
    "Carla": "20101"
}
#Para agregar algo
agenda["Juan"]= "0303020"

# Para eliminar 
del agenda["Ana"]

# Mostrar el numero de un contacto epecifico
print("Telefono de Bruno", agenda["Bruno"])
nombre= input("Ingrese el nombre de la persona")
if nombre in agenda: 
    print("Telefono de:" +nombre agenda[nombre])
else: 
    telefono= input("Ingrese el telfeno")
    agenda[nombre]= telefono # Aqui agregamos a un nuevo usuario
    print("Ese nombre no esta en la lista")

#Podemos usar un condicional para verificar si alguna clave esta en el diccionario 
if "Juan" in agenda: 
    print("Si esta")
else: 
    print("No esta")
#para enseñar el diccionario 
print("El diccionario es", agenda)
""" 
"""
estudiantes = { 
    "Lucia": [4.4,2.3,2.3,4],
    "Mateo": [3.0,3.4,3.5,5],
    "Sofia": [5,4.5,3.4,4.3]
}
promedios={}
for nombre, notas in estudiantes.items():
    print(nombre, notas)
    prom= sum(notas)/len(notas)
    print(f"promedio de {nombre}:{prom:.2f}")
    promedios[nombre]=prom
print(promedios)

mejor_estudiante= max(promedios, key=promedios.get)
print(f"El estudiante con mejor promedio es: {mejor_estudiante}")
"""
# Ejercicio 
inventario={ 
    "cuaderno": 15 ,
    "lapiz": 40,
    "borrador": 0,
    "marcador": 10,
    "regla": 5, 
}
inventario= {}
print(" Bienvenido al sistema de papeleria")
print("selecciones una opcion")
print("1. Agregar")
print("2. vender")
print("3. Mirar productos")
opcion= int(input("Ingrese su opcion"))
if opcion== 1: 
    nombre = input("Ingrese el nombre del producto")
    cantidad= int(input("Ingrese la cantidad de productos a agregar"))
    if nombre in inventario: 
        inventario[nombre] += cantidad
    else: 
        inventario[nombre]= cantidad 
    print("El inventario fue actualizado")
if opcion == 2: 
    nombre_v= input("Ingrese el nombre del producto")
    if nombre_v in inventario: 
        cantidad_v= int(input("Ingrese la cantidad a comprar"))
        if inventario(nombre_v) >= cantidad:
            inventario[nombre_v] -= cantidad_v
            print("inventario actualizado")
    else: 
        print("No hay cantidad suficiente")

else: 
    print("producto no exite")
if opcion== 3: 
    print(inventario)
if opcion == 0:
    print("Hasta luego")
    
else: 
    print("Opcion no permitida")
