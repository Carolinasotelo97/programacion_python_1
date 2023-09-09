'''Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.' '''

edad = int(input('Ingrese su edad: '))
#parseo  el int 
edad = int(edad)
eCivil= input('Ingrse su estado civil: ')

if edad < 18 and eCivil != "Soltero":
    print("Eres muy pequeño para NO ser soltero.")
else:
    print("Eres mayor de edad para poder tener pareja.")