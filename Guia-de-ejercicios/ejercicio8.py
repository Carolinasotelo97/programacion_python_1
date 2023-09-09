'''Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido'''

#inicializo la lista
lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

contador = 0

#recorro la lista numeros con el for
#para encontrar un numero repetido tenes que hacer si o si 2 for
for numero in lista_numeros:
    for dato in lista_numeros:
        if numero == dato:
            contador += 1

if contador == 2:
    print(numero)