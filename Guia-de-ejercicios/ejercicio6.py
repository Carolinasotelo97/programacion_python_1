'''Ejercicio 6:
Utilizar For
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
mostrar el mayor.'''

#declaro una variable llamada lista
lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
#declaro una variable que no tiene datos = None (none es un dato que no tiene nada)
mostrar_mayor = None 

# for recorre la lista de numeros y por cada numero que recorre la guarda en la variable numero
for numero in lista:
    if mostrar_mayor == None or numero > mostrar_mayor:
        mostrar_mayor = numero
print(mostrar_mayor)

#hacer lo mismo con indices el ranga trabaja con los indices
'''
lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

nota_mayor = lista_numeros[0]

for inidice in range(len(lista_numeros)):
    if lista_numeros[indice] > nota_mayor:
            nota_mayor= lista_numeros[indice]
    print(nota_mayor)
'''