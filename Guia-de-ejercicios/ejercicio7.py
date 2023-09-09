'''Ejercicio 7:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar solo los números pares.'''

numeros_lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

numeros_pares = 0

for numero in numeros_lista:
    if numero %2 == 0:
        numeros_pares +=1
        pares = numero
        print("NUmero par: {}" .format(pares))

print("Cantidad pares: {}" .format(numeros_pares))