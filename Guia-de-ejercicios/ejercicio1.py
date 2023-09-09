'''Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.'''

#ingreso de datos
nombre = input('nombre: ')  #el input es una funcion de ingreso por teclado
sueldo = input('sueldo: ')
#parseo sueldo
sueldo = float(sueldo)

#valido que no ingrese 0 o negativos
while sueldo <=0:
    sueldo = input('Sueldo mayor a 0')
    # vuelvo a parsear sueldo
    sueldo = float(sueldo)

#guardo dentro de la variable aumento_sueldo el calculo
aumento_sueldo = sueldo + sueldo * 0.1

# y la imprimo
print(f"El sueldo {sueldo} con un 10% mas es: {aumento_sueldo}")

