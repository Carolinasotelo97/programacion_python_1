'''Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos'''

#declaro el precio base
tarifa = 15000
#me guardo el precio base en otra variable para despues calcular con descuento
tarifa_descuento = tarifa

#pido un input para cada uno
ingreso_estacion = input("Ingrese una estacion del año: ")
#valido la estacion elegida
while ingreso_estacion != "Invierno" and ingreso_estacion  != "Verano" and ingreso_estacion != "Otonio" and ingreso_estacion != "Primavera":
    ingreso_estacion = input("Ingrese una estacion valida")

ingreso_localidad = input("Ingrse una localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ")
#valido localidad elegida
while ingreso_localidad != "Cataratas" and ingreso_localidad != "Mar del Plata" and ingreso_localidad != "Cordoba" and ingreso_localidad != "Bariloche":
    ingreso_localidad = input("Ingrese una localidad valida")

''' Porcentajes:
Si multiplicas algo por 0.20 es lo mismo que sacar el 20% de ese número.
Si a vos lo que te interesa es saber cuánto sería el valor de un número más el 20% de ese mismo número, podés hacer: numero * 1.20'''
   
if ingreso_estacion == 'Invierno':
    if ingreso_localidad == 'Bariloche':
        tarifa_descuento *= 1.2
        print("Bariloche tiene un aumento del 20% en invierno el precio total es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Cataratas' or ingreso_localidad == 'Cordoba':
        tarifa_descuento *= 0.9
        print("Cataratas y Córdoba tiene un descuento del 10% en invierno. El precio final es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Mar del Plata':
        tarifa_descuento *= 0.8 
        print("Mar del Plata tiene un descuento del 20%. El precio final es: ${}" .format(tarifa_descuento))

if ingreso_estacion == 'Verano':
    if ingreso_localidad == 'Bariloche':
        tarifa_descuento *= 0.8
        print("Bariloche tiene un descuento del 20% en invierno el precio total es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Cataratas' or ingreso_localidad == 'Cordoba':
        tarifa_descuento *= 1.1
        print("Cataratas y Córdoba tiene un aumento del 10% en invierno. El precio final es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Mar del Plata':
        tarifa_descuento *= 1.2
        print("Mar del Plata tiene un aumento del 20%. El precio final es: ${}" .format(tarifa_descuento))

if ingreso_estacion == 'Otonio' and ingreso_estacion == 'Primavera':
    if ingreso_localidad == 'Bariloche':
        tarifa_descuento *= 0.8
        print("Bariloche tiene un decuento del 20% en invierno el precio total es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Cataratas':
        tarifa_descuento *= 1.1
        print("Cataratas tiene un aumento del 10% en invierno. El precio final es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == 'Mar del Plata':
        tarifa_descuento *= 1.1
        print("Mar del Plata tiene un aumento del 10%. El precio final es: ${}" .format(tarifa_descuento))
    elif ingreso_localidad == "Cordoba":
        tarifa = tarifa
        print("Cordoba en esas estaciones no tiene descuentos ni aumentos. El precio final es: ${}" .format(tarifa))