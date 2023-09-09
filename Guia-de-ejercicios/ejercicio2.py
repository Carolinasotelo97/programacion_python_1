'''Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).'''

edad = input('Ingrese una edad: ')

while edad.isdigit() == False:
    print("Dato Invalido.")
    edad = input("Reingresa una edad: ")
   
edad = int(edad)  

if edad > 17:
    print("Es mayor de edad")
elif edad >12:
    print("Es adolescente")
else:
    print("Es niño menor de edad")