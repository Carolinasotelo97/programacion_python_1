from stark_biblioteca import*
from data_stark import lista_personajes
import re

#punto 0
def stark_normalizar_datos(lista_personajes):
    if not lista_personajes: #verifico que la lista de heroes está vacia o no tiene ningun elemento
        print("No se puedieron normalizar los datos. Intentelo de nuevo.\n") #si está vacia, devuelve este error
        return False #devuelve False que no se pudieron normalizar los datos.
    
    datos_modificados = False #creo una variable y la inicializo en False para poder trackear si se modificaron los datos despues

    for heroe in lista_personajes: #recorro la lista de heroes y la guardo en la variable heroe 
        if "fuerza" in heroe: #verifico si hay alguna clave llamada fuerza
            nuevo_valor = str(heroe["fuerza"]) #si la tiene, la guardo en una nueva varible como cadena de texto para poder usar una expresion regular
            if re.search(r'^[0-9]+(\.[0-9]+)?$', nuevo_valor): #utilizo el metodo re.search para ver si el valor es un numero valido. Utilizo la expresion regular para verificar si la cadena es un int o es float valido.
                heroe["fuerza"] = int(heroe["fuerza"]) #si es valido, entra al if convertimos ese valor en un int y actualizo la clave
                datos_modificados = True #cambio a True para saber que se modifico un dato
        
        for clave in ["altura", "peso"]: # Utilizo CLAVE para acceder directamente a las claves del diccionario y recorro en este caso, las claves altura y peso para verificar si existen.
            if clave in heroe: 
                nuevo_valor = str(heroe[clave]) #si existe, convierto esos valores en cadena de texto para usar nuevamente el metodo re.search
                if re.search(r'^[0-9]+(\.[0-9]+)?$', nuevo_valor): #y valido que sea un float o int
                    heroe[clave] = float(heroe[clave]) #si entra en el if, me guardo el nuevo valor en un float
                    datos_modificados = True #modifico a true para saber que se modifico el dato
    
    if datos_modificados: #verificamos si los datos son verdaderos. 
        print("Los datos fueron normalizados correctamente!\n") #Si los son, entro al if diciendo que se normalizaron correctamente
        return True
    else:
        print("Hubo un error al normalizar los datos. Inténtelo de nuevo.\n") #de lo contrario, lanzara error
        return False
    
# 1.1
def obtener_dato(un_heroe: dict, clave: str): #le paso dos argumentos, un diccionario y un string
    if clave in un_heroe: #verifico si la clave existe
        return un_heroe[clave] #si la clave existe, devuelve el valor que esta asociado a esa clave
    return None #si no existe, devuelve none

#punto 1.2
def obtener_nombre(heroe: dict): #le paso el argumento heroe que es un diccionario
    nombre = obtener_dato(heroe, "nombre") #almaceno en la variable nombre con el dato obtenido con el nombre
    if nombre: #verifico si se pudo obtener el dato para el nombre
        return f"\nNombre:{nombre}\n" #si se obtuvo el dato, muestro el nombre
    return False #si no se pudo obtener el dato, devuelve False

    
def mostrar_heroe_nb(lista_personajes): #le paso la lista de personajes
    heroes_nb_encontrados = False #inicializo esta variable en False para poder usarla despues si encontre uno en la lista
    
    for heroe in lista_personajes: #recorro los heroes en la lista de personajes
        genero_heroe = obtener_dato(heroe, "genero") #almaceno en la variable genero_heroe el dato obtenido en la lista segun la clave genero
        if genero_heroe and genero_heroe.upper() == "NB": #verifico que exista el genero NB en la lista. le paso upper para que sea indistinta la mayusculas y minusculas.
            nombre_heroe = obtener_nombre(heroe) #si esto es verdadero, me guardo el nombre nuevo del superheroe con genero NB en mi varibale nombre_heroe
            if nombre_heroe: #verifico si se obtuvo un nombre
                print(f"Superhéroe de género NB encontrado: {nombre_heroe}") #si es verdadero me muestra el nombre del superheroe con genero NB
                heroes_nb_encontrados = True #actualizo a true para marcar que encontre uno
    
    if not heroes_nb_encontrados:
        print("No se encontraron superhéroes de género NB.\n")

#2
def obtener_nombre_y_dato(heroe: dict, clave:str): #le paso el argumento heroe que es un diccionario
    nombre = obtener_nombre[heroe] #llamo a mi funcion obtener_nombre y guardo el nombre en la variable
    if nombre: #verifico si se pudo obtener el dato para el nombre
        if clave in heroe: #verifico que exista la clave
            dato = heroe[clave] #si existe, guardo la clave
            return f"\nNombre:{nombre}\n {clave}: {dato}" #si se obtuvo el dato, muestro el nombre
        else:
            return False
    return False #si no se pudo obtener el dato, devuelve False

#3.1
def obtener_maximo(lista_personajes: dict, clave:str): #le paso dos parametros

    maximo_valor = None  # Inicializo el valor máximo como None para despues marcar cuando encuentre el maximo valor

    for elemento in lista_personajes: #recorro cada elemento en la lista heroes
        if clave in elemento: #verifico si existen claves en elementos
            valor = elemento.get(clave, None) #obtenemos el valor de la clave en el elemento 
            if valor is not None and (maximo_valor is None or valor > maximo_valor): #verifico si la clave ingresada existe o si da None    
                maximo_valor = valor #si existe, la guardo en mi variable maximo valor 

    return maximo_valor

#3.2
def obtener_minimo(lista_personajes: dict, clave:str): #le paso dos parametros

    minimo_valor = None  # Inicializo el valor máximo como None para despues marcar cuando encuentre el minimo valor

    for elemento in lista_personajes: #recorro cada elemento en la lista heroes
        if clave in elemento: #verifico si existen claves en elementos
            valor = elemento.get(clave, None) #obtenemos el valor de la clave en el elemento 
            if valor is not None and (minimo_valor is not None and valor < minimo_valor): #verifico si la clave ingresada existe o si da None    
                minimo_valor = valor #si existe, la guardo en mi variable minimo valor 
                minimo_valor = True

    return minimo_valor

def obtener_dato_cantidad(lista_personajes, dato, clave):
    if not lista_personajes: #verifico si la lista esta vacia
        print("La lista está vacía. No se puede obtener héroes") #si está vacia muestra mensaje de error
        return [] #y devuelve una lista vacia
    
    if clave not in lista_personajes[0]: #verifico que la clave exista en el primer elemento de la lista
        print("La clave '{0}' no existe en la lista de personajes." .format(clave)) #si no existe, muestra el mensaje de error 
        return[] #y devuelve una lista vacia
    
    resultado = [] #creo una lista vacia en donde voy a guardar la lista de heroes que si cumplan con las condiciones
    
    valor_maximo = obtener_maximo(lista_personajes, clave)
    valor_minimo = obtener_minimo(lista_personajes, clave)

    

    for heroe in lista_personajes: #recorro la lista
        valor = heroe.get(clave) #obtengo el valor de clave del heroe actual 
        if valor == dato: #verifico si el valor obtenido es igual al dato que busco 
            resultado.append(heroe) #si coincide, lo agrego a mi lista resultados

    return resultado #retorna la lista de resultados que fui cargando.

#3.4
def stark_imprimir_heroes(lista_personajes):
    if not lista_personajes:  # Verifico si la lista de heroes esta vacia
        print("La lista de heroes esta vacia. No hay informacion para mostrar.")
        return False
    
    for heroe in lista_personajes:  # Si la lista no está vacia recorror cada heroe en la lista de heroes
        print("Informacion:\n")
        for clave, valor in heroe.items():  #recorro claves y valores del heroe
            print("{0}: {1}".format(clave, valor))  # Imprime la clave y su valor
    
    return True

#4.1
def sumar_dato_heroe(lista_personajes, clave):

    suma_heroes = 0 #incializo en 0 para poder hacer la suma

    for heroe in lista_personajes: #recorro cada heroe a traves de la lista de heroes 
        if type(heroe) == dict and clave in heroe: #verifico si heroe es un diccionario y si tiene una clave
            valor = heroe.get(clave) #si es un diccionario, me guardo el valor 
            if (type(valor) == int or type(valor) == float): #verifico si es un valor numerico
                suma_heroes += valor #y si lo es, lo sumo

    return suma_heroes # Devolvemos la suma total de los valores encontrados

#4.2
def dividir(dividendo, divisor):
    if divisor == 0: #verifico que el divisor no sea 0
        return False #si lo es, devuelve falso
    
    resultado = dividendo / divisor  # de lo contrario, guardo en mi variable resultado la division

    return resultado

#4.3
def calcular_promedio(lista_personajes, clave):
    suma = sumar_dato_heroe(lista_personajes, clave) # Utilizamos la función sumar_dato_heroe para obtener la suma de los valores
    cantidad = len(lista_personajes) #guardo en la variable cantidad, la cantidad de heroes

    if cantidad == 0: #verifico si la lista esta vacia
        return None  # Si a lista esta vacia, retorno None para evitar la división por cero si no se encuentra ningún valor válido.

    promedio = dividir(suma, cantidad) #guardo en la variable promedio la division entra la suma obtenida y la cantidad
    return promedio #y retorno el mismo

#4.4
def mostrar_promedio_dato(lista_personajes, clave):
    if not lista_personajes:  # Valido si la lista de heroes esta vacia
        return False  # Si la lista esta vacia, retorna False

    valores = []  # Inicializo una lista vacia para almacenar los valores encontrados

    for heroe in lista_personajes:  # recorro la lista de heroes segun cada heroes
        if clave in heroe:  # Verifico si la clave especificada existe en el heroe
            valor = heroe[clave]  # Obtengo el valor asociado a la clave
            if type(valor) == int or type(valor) == float:  # Verifico si el valor es de tipo numerico
                valores.append(valor)  # Si es un valor numerico, lo agrego a la lista de valores

    if not valores:  # Verifico si no se encontraron valores validos
        return False  # Si no se encontraron valores validos, retorna False

    suma = sumar_dato_heroe(valores, clave)  # Utilizo la función sumar_dato_heroe para sumar los valores obtenidos
    cantidad = len(valores)  # Obtengo la cantidad de valores validos encontrados

    promedio = dividir(suma, cantidad)  # Utilizo la función dividir para calcular el promedio de ambos 

    return promedio  # Develve el promedio calculado