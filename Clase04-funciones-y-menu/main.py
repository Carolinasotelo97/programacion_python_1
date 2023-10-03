#menu
from funciones import * #el asterisco me dice que importe todo el archivo

flag = True

while(flag):
    print("Elija que operacion quiere realizar: \n",
        "1. Suma \n",
        "2. Resta \n",
        "3. Multiplicacion \n",
        "4. Division \n",
        "5. Salir \n")
    respuesta = input("Ingrese una opcion: ")

match(respuesta):
    case "1":
      numero_1 = int(input("Ingrese el primer numero: "))
      numero_2 = int(input("Ingrese el segundo numero: ")) #casteamos el numero para que nos devuelva un numero y no un string
      resultado = sumar(numero_1, numero_2)
      print(resultado) #forma de imprimir 1
    case "2":
      numero_1 = int(input("Ingrese el primer numero: "))
      numero_2 = int(input("Ingrese el segundo numero: "))
      print(restar(numero_1, numero_2)) # forma de imprimir 2
    case "3":
      numero_1 = int(input("Ingrese el primer numero: "))
      numero_2 = int(input("Ingrese el segundo numero: "))
      print(multiplicar(numero_1, numero_2))
    case "4":
      numero_1 = float(input("Ingrese el primer numero: "))
      numero_2 = float(input("Ingrese el segundo numero: "))
      print(dividir(numero_1, numero_2))
    case "5":
      flag = False
    case _:
        print("Ingrse una opcion valida. \n")