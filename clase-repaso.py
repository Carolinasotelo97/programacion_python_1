#declarar una variable

numero = 2


otra_variable = "segundo"

mes = "abril"

continuar = True

#operadores logicos 
# && ---> and
# || ---> or
# ! ---> not

if numero == 2 and otra_variable == "segundo":
    print("si es un dos")
    #todo lo que escriba aca dentro
    #es parte el if
elif numero > 5:
    print("es mayor a 5")
else:
    print("estoy en el else")



while continuar == True:
    #se ejecuta el bucle
    continuar = False

match mes:
    case 'abril':
        print('estamos en abril')
    case 'mayo':
        print('estamos en abril')
    case _:
        print('estamos en el default')
        

while continuar == True:
    #se ejecuta el bucle
    continuar = False

#[0,1,2,3,4,5,6,7,8,9] ---> lista de numeros
# 1,2,3,4,5,6,7,8,9,10 contador de elementos
for numero in range(10): #0 al 9 
    #print("el numero es: ")
   # print(numero)
    #print(f"El numero es ${numero}")
    print("el numero es {0}".format(numero))



edad = 12
nombre = "marina"
altura = 1.70

print("edad")
print(type(edad))
print("nombre")
print(type(nombre))
print("altura")
print(type(altura))


'''
en c

int numeros[10]

[0,1,2,3,4,5,6,7,8,9] elementos
 0,1,2,3,4,5,6,7,8,9 INDICES
 1,2,3,4,5,6,7,8,9,10 contador de elementos

numeros = []

[0,1,"marina",3,True,5,[1,2],7,8,9]
 0,1,2       ,3,4   ,5,6    ,7,8,9 INDICES

   

#crear una lista
numeros = []
numeros_lista = list()

#agregar
numeros.append(10)
numeros.append(67)
numeros.append("pedro")

print(numeros)
'''

nombres = []
edades = []
alturas = []

for numero in range(3):

    nombre = input("Ingrese un nombre: ")
    while type(nombre) == None:
        print("No ingresaste nada")
        nombre = input("Ingrese un nombre: ")

    edad = input("Ingrese una edad: ")
    while edad.isdigit() == False:
        edad = input("Ingrese una edad: ")
    edad = int(edad)

    altura = input("Ingrese una altura: ")
    altura = float(altura)

    nombres.append(nombre)
    edades.append(edad)
    alturas.append(altura)

print(nombres)
print(edades)
print(alturas)

tam_lista = len(nombres) #como obtener el tamaño de una lista

for indice in range(tam_lista):

    #si son mayores de 30 años lo imprimo 
    if edades[indice] > 30:
        print("Los nombres son: {0}".format(nombres[indice]))





