def sumar(numero_1: int, numero_2: int =2)-> int:
    '''
    Documentacion: suma dos numeros enteros y nos devuelve el resultado de ellos.
    '''
    return numero_1 + numero_2

def restar(numero_1: int, numero_2: int =2)-> int:
    '''
    Documentacion: resta dos numeros enteros y nos devuelve el resultado de ellos.
    '''
    return numero_1 - numero_2

def multiplicar(numero_1: int, numero_2: int =2)-> int:
    '''
    Documentacion: multiplica dos numeros enteros y nos devuelve el resultado de ellos.
    '''
    return numero_1 * numero_2

def dividir(numero_1: int, numero_2: int =2)-> int:
    '''
    Documentacion: divide dos numeros enteros y nos devuelve el resultado de ellos.
    '''
    if numero_2 != 0: 
        return numero_1 / numero_2