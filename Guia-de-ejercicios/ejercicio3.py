'''Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.'''

contador = 0
lista_numeros =[] #creamos una lista vacia 

#le pido 5 veces que ingrese un numero con el while
while contador < 5: 
    contador += 1
    #pido un numero
    numero= input('Ingrese un numero entero: ')
    #siempre que pido un numero lo parseo
    numero = int(numero)
    
    while numero == 0:
        numero= input('Error. Ingrese un numero distinto de 0: ')
        numero = int(numero)

    #agrego a la lista los 5 numeros pedidos por el while
    lista_numeros.append(numero)


#inicializamos
contador_pares = 0
contador_impares = 0
minimo = None
maximo_pares = None
flag_par = False
suma_positivos = 0
flag_negativos = False
productos_negativos =1

for numero in lista_numeros:
    #a
    if numero %2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    #b
    if minimo == None or numero < minimo:
        minimo = numero
    #c   
    if numero % 2 == 0:
        if maximo_pares == None or numero > maximo_pares:
            maximo_pares= numero
            flag_par = True #si se cumple esta condicion es true
    #d
    if numero > 0:
        suma_positivos += numero
    #e
    if numero < 0:
        productos_negativos *= numero
        flag_negativos = True


print("Hay {0} numeros pares y {1} numeros impares" .format(contador_pares, contador_impares)) #el orden de los numeros dentro de las llaves es relacion con lo primero que se imprime en el .format
print("El menor numero ingresado es: {0}" .format(minimo))
if flag_par == True:
    print("El mayor numero par es: {0}" .format(maximo_pares))
else:
    print("No se ingresaron numeros pares.")

print("La suma de los numeros positivos es {0}" .format(suma_positivos))
if flag_negativos == True:
    print("El prodcuto de los numeros negativos es {0}" .format(productos_negativos))
else:
    print("No se ingresaron numeros negativos")