'''Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.

Ejemplo de mensaje de consola:'''

tipos= []
precios = []
cantidades = []
marcas = []
fabricantes = []
contador =0

max_barbijo = None
max_unidades = None
unidades_jabon = 0

#ingreso y validacion de datos
for contador in range(5):
    contador += 1
    
    carga_tipo = input("Ingrese un producto (barbijo, jabon o alcohol): ")
    while carga_tipo != "barbijo" and carga_tipo != "jabon" and carga_tipo != "alcohol":
        carga_tipo = input("Ingrese un tipo correcto ")

    carga_precio = float(input("Ingrese el precio del producto: "))
    while carga_precio <100 or carga_precio > 300:
        carga_precio = float(input("Ingrese un precio dentro del rango 100 a 300: "))

    carga_cantidad = int(input("Ingrese la cantidad de unidades: "))
    while carga_cantidad <= 0 and carga_cantidad > 1000:
        carga_cantidad = int(input("Ingrese una cantidad que no sea 0 ni negativo y no debe superar las 1000 unidades: "))

    carga_fabricante = input("Ingrese el fabricante: ")

    carga_marca =  input("Ingrese la marca: ")

    tipos.append(carga_tipo)
    precios.append(carga_precio)
    cantidades.append(carga_cantidad)
    marcas.append(carga_marca)
    fabricantes.append(carga_fabricante)



#buscar e informar
#len es para que lea el tamaño de la lista "tipos" y la recorre las listas
for i in range(len(tipos)):

    #A
    if tipos[i] == "barbijo":
        if max_barbijo == None or precios[i] > max_barbijo:
            max_barbijo = precios[i]
            cantidad_unidades_barbijo = cantidades[i]
            fabricante_barbijo = marcas[i]
    
    #C
    elif tipos[i] == "jabon":
        unidades_jabon += cantidades[i] #acumulador de unidades de jabon

    #B
    if max_unidades == None or cantidades[i] > max_unidades:
        max_unidades = cantidades[i]
        max_f_unidades = marcas[i]
        nombre_tipo_cantidades = tipos[i]

print("El barbijo mas caro tiene un precio de ${} con {} unidades de la marca{}" .format(max_barbijo, cantidad_unidades_barbijo, fabricante_barbijo))
print("El producto con mas unidades es el {} con {} unidades de la marca {}" .format(nombre_tipo_cantidades, max_f_unidades, max_unidades))
print("Hay un total de {} jabones" .format(unidades_jabon))