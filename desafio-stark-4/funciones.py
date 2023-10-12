import re
from data_stark import lista_personajes
#1.1
def extraer_iniciales(nombre_heroe):
    if not nombre_heroe: #verifico que nombre_heroe este vacio 
        return 'N/A' #retorna N/A si está vacio

    iniciales = re.findall(r'\bthe\b|\b-\b|(\b\w)', nombre_heroe) #uso re.findall para encontrar todos los heroes con la palabra "the" o que contengan "-" y todas las iniciales de las palabras y las guardo en la variable Iniciales
    #\b\w -> busca todas las primeras letras de las palabras

    iniciales_filtradas = [] #creo una nueva lista vacia para almacenar las iniciales de los hereos encontrados

    for inicial in iniciales: #recorro las iniciales por cada incial encontrada
        if inicial: #verifico que la inicial no este vacia
            iniciales_filtradas.append(inicial.upper()) #si no esta vacia, la conviertoe en maysuculas y las agrego a la lista iniciales_filtradas
    
    iniciales_encontradas = '.'.join(iniciales_filtradas) #uso .join para unir las iniciales que encontre con un "." y las guardo en una nueva variable iniciales_encontradas

    return iniciales_encontradas #retorno las iniciales encontradas

#1.2
def definir_iniciales_nombre(heroe):
    resultado = {}  # Inicializo un diccionario vacío en la variable resultado

    if type(heroe) == dict:  #verifico que heroe sea de tipo diccionario
        nombre_heroe = heroe.get('nombre', '') #si lo es, obtengo el valor de la clave nombre y lo guardo en una variable nombre_heroe

        if nombre_heroe: #verifico que nombre_heroe no sea None
            iniciales = extraer_iniciales(nombre_heroe) #si no lo es, llamo a mi funcion extraer iniciales y le paso como parametro nombre_heroe y lo guardo en una variable iniciales
 
            if iniciales != 'N/A': #verifico que las iniciales obtenidas no sean N/a
                heroe['iniciales'] = iniciales #si no lo es, agrego la clave 'iniciales' con su valor al diccionario de heroes
                resultado = heroe #retorno el diccionario

    return resultado

#1.3
def agregar_iniciales_nombre(lista_heroes):
    if lista_heroes is None or len(lista_heroes) == 0 or type(lista_heroes) is not list:
        print("El origen de datos no contiene el formato correcto")
        return []  # Devolver una lista vacía en caso de error

    nombres_con_iniciales = []  # Lista para almacenar los nombres con iniciales

    for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
        resultado = definir_iniciales_nombre(heroe)  #llamo a mi funcion definir_iniciales_nombre y le paso hereo como parametro y lo guardo en una varibale de resultado

        if resultado is not None:  # Verificar si el resultado no es None
            nombres_con_iniciales.append(resultado)  # Agregar el nombre con iniciales a la lista

    return nombres_con_iniciales  # Devolver la lista de nombres con iniciales

#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if lista_heroes is None or len(lista_heroes) == 0 or type(lista_heroes) is not list: #verifico que la lista de heroes tiene al menos un elemento, es none o si es una lista
        print("El origen de datos no contiene el formato correcto") #si esta vaicia devuelve el mensaje
        return False

    for heroe in lista_heroes: #recorro la lista de heroes segun cada heroe
        resultado = definir_iniciales_nombre(heroe) #llamo a mi funcion definir_iniciales_nombre para obtener la info de iniciales por nombre de heroe y la guardo en una variable de resultado

        if resultado is not False:  #verifico que no sea False 
            nombre = resultado['nombre'] #Si no es false, obtengo el nombre del heroe del diccionario
            iniciales = resultado['iniciales'] #obtengo las inciales
            print(f"* {nombre} ({iniciales})")#imprimo la lista de nombres con sus iniciales

    return True

#2.1
def generar_codigo_heroe(id_heroe, genero_heroe):
    # Validar que el id_heroe sea numérico y el género sea válido
    if not (type(id_heroe) == int) or genero_heroe not in ['M', 'F', 'NB']:
        return "N/A"

    # Formatear el código con el género y el id_heroe, llenando con ceros
    codigo = f"{genero_heroe}-{str(id_heroe).zfill(8)}"

    if len(codigo) != 10:  # Verificar si el código tiene exactamente 10 caracteres
        return "N/A"

    return codigo

#2.2
def generar_codigo_heroe(id_heroe, genero_heroe):
    if not id_heroe: #verifico que no exista un id_heroe
        return "N/A" #si no existe, arroja N/A
    
    if genero_heroe != "M" and genero_heroe != "F" and genero_heroe != "NB": #verifico que no existan los generos pasados
        return "N/A" #si no existe, arroja N/A

    
    codigo = f"{genero_heroe}-{str(id_heroe).zfill(8)}" #convierto id_heroe en str para poder pasarle el metodo zfill y que rellene los digitos con 0 a la izquierda y le paso el genero concatenado con "-" y lo guardo en una varibale codigo

    if len(codigo) > 10: #verifico que el codigo tenga una longitud de 10 caracteres totales
     return "N/A"

    return codigo
# 2.3
def stark_generar_codigos_heroes(lista_heroes):
    if not lista_heroes: #verifico que la lista  este vacia
        print("El origen de datos no contiene el formato correcto")
        return

    cantidad_codigos = 0 #inicializo el contador de codigos para luego sumarlos
    primer_id = 1 #inicializo el primer_id en 1 para luego incrementar

    for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
        if 'genero' not in heroe or type(heroe) is not dict: #verifico que la calve genero este en el diccionario y que heroe sea de tippo diccionario
            print("El origen de datos no contiene el formato correcto") #si no cumple, devuelve el mensaje de error
            return

        genero_heroe = heroe['genero'] #obtengo el genero del diccionario heroe y lo guardo en una nueva variable
        codigo = generar_codigo_heroe(primer_id, genero_heroe) #llamo a mi funcion generar_codigo_heroe para generar el codigo del heroe y lo guardo en una variable codigo

        heroe['codigo_heroe'] = codigo #agrego la nueva clave "codigo_heroe" a el diccionario hereo y le guardo su valor codigo
        cantidad_codigos += 1 #incremento el contador
        primer_id += 1

    if cantidad_codigos > 0: #verifico que se haya generado el codigo 
        print(f"Se asignaron {cantidad_codigos} códigos")
        print(f"* El código del primer héroe es: -M-{str(1).zfill(8)}")#imrpimo el codigo, lo convierto en str para poder usar el metodo zfill y que rellene con 0 a la izquierda
        print(f"* El código del último héroe es: M-{str(primer_id - 1).zfill(8)}")



#3.1
def sanitizar_entero(numero_str):
    numero_str = numero_str.strip()  # elimina espacios en blanco al principio y al final de numero_str
    if numero_str[0] == '-': #verifico que el primer caracter sea un "-" para verificar los numeros negativos
        return -2  # Número negativo
    if numero_str.isdigit(): #verifico que los caracteres de numero_str sean numericos
        return int(numero_str) #y devuleve el numero entero
    else:
        return -1  # Contiene caracteres no numéricos

#3.2
def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip()  # elimino espacios en blanco al principio y al final
    if numero_str[0] == '-':#verifico que el primer caracter sea un "-" para verificar los numeros negativos
        return -2  # Número negativo
    separador = numero_str.split('.')#divido el numero usando el metodo split con y lo guardo en una varibale separador
    if len(separador) == 2 and separador[0].isdigit() and separador[1].isdigit(): #verifico que la longitud del separador sea de 2 y que la primera posicion sea un digito entero y que la segunda parte sea un numero entero
        valor = float(numero_str) #si cumple, guardo el numero float en una variable valor
        if valor >= 0: #verifico que el valor sea positivo
            return valor
    return -1  # Contiene caracteres no numéricos o no es un número flotante válido


#3.3
def sanitizar_string(valor_str, valor_por_defecto='-'):
    valor_str = valor_str.strip() #elimino los espacios en blanco y lo guardo
    
    if not valor_str: #verifico que no este vacio
        return valor_por_defecto.lower() #si esta vacio devuelve el valor por defecto "-"
    
    valor_str = valor_str.replace('/', ' ') #uso el metodo replace para reemplazar en donde haya una / por un espacio en blanco y lo guardo en mi variable valor_str
    
    numeros = False #inicializo numeros en False para verificar si hay numeros 
    
    for caracteres in valor_str: #recorro la cadena de valor_str segun cada caracter
        if caracteres.isdigit(): #verifico que no sea un digito
            numeros = True #si lo es, devuelve True numeros
    
    if numeros == True: #verifico que numero sea true
        return "N/A" #si lo es, devuelve N/A
    
    return valor_str.lower() #devuelvo el valor de valor_str y lo paso todo a minusculas

#3.4
def sanitizar_dato(heroe, clave, tipo_dato):
    
    clave = clave.lower() # Convierte la clave a minusculas y la guardo en la varible clave
    
    if tipo_dato.lower() != 'string' and tipo_dato.lower() != 'entero' and tipo_dato.lower() != 'flotante': #verifico que el tipo de dato no sea String, Entero o Flotante
        print('Tipo de dato no reconocido') #si no es ninguna de las anteriores devuelve el error
        return False #retorna False para indicar que hubo un error

    if clave not in heroe: #verico que clave exista en la lista
        print('La clave especificada no existe en el héroe') #si no existe, imprimo el error
        return False #retorno falso para indicar que hubo un error

    valor = heroe[clave] #obtengo el valor de la clave en el diccionario y lo guardo en una variable valor

    if tipo_dato.lower() == 'string': # verifico si el tipo_dato es string
        heroe[clave] = sanitizar_string(valor) #llamo a mi funcion sanitizar_string y le paso el valor obtenido
    elif tipo_dato.lower() == 'entero':# verifico si el tipo_dato es entero
        resultado_entero = sanitizar_entero(valor)#llamo a mi funcion sanitizar_entero y le paso el valor obtenido
        if resultado_entero is not None:
            heroe[clave] = resultado_entero
        else:
            print(f'Error: No se pudo convertir a entero la clave "{clave}" con valor "{valor}"')
            return False
    elif tipo_dato.lower() == 'flotante':# verifico si el tipo_dato es flotante
        resultado_flotante = sanitizar_flotante(valor)#llamo a mi funcion sanitizar_float y le paso el valor obtenido
        if resultado_flotante is not None:
            heroe[clave] = resultado_flotante
        else:
            print(f'Error: No se pudo convertir a flotante la clave "{clave}" con valor "{valor}"')
            return False
    
    print('Clave: {0} - sanitizada: {1}'.format(clave, heroe[clave]))
    return True


#3.5
def stark_normalizar_datos(lista_heroes):
    if not lista_heroes: #verifico que la lista_heroes este vacia
        print("Error: Lista de héroes vacía") #si lo esta, imprimo el mensaje de error 
        return False #retorna False para indicar que esta vacia

    for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
        for clave in heroe: #recorro las claves de cada heroe
            if clave in ["altura", "peso", "color_ojos", "color_pelo", "fuerza", "inteligencia"]: #verifico si estan las claves solicitadas
                if clave in ["altura", "peso"]: #verifico el tipo de dato de estas claves
                    tipo_dato = "flotante" #si existen estas claves, les digo que son flotantes
                else:
                    if clave in ["fuerza"]: #verifico que el tipo de dato de la clave Fuerza sea entero
                        tipo_dato = "entero" #si lo es, le digo que es entero
                    else:
                        tipo_dato = "string" #de lo contrario sera un string
                sanitizar_dato(heroe, clave, tipo_dato) #llamo a mi funcion sanitizar_dato y le paso los argumentos heroe, clave y tipo_dato y normalizo el dato 

    print("\nDatos normalizados!")

#4.1
def generar_indice_nombres(lista_heroes):

    if not lista_heroes:#verifico que la lista_heroes este vacia
        print("Error: Lista de héroes vacía") #si lo esta, imprimo el mensaje de error 
        return False #retorna False para indicar que esta vacia

    for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
        if not (type(heroe) is dict and 'nombre' in heroe): #verifico que heroe sea de tipo diccionario y que exista la clvae nombre
            print("El origen de datos no contiene el formato correcto") #si no se existe, o no se cumple imrpime el error
            return False
    
    nueva_lista =[] #genero una lista vacia para guardar los elementos

    for heroe in lista_heroes: #recorrro cada heroe en la lista_heroes
        nombre = heroe['nombre'] #obtengo el valor de la clave nombre y la guardo en una varible nombre
        palabras_separadas = nombre.split() #usando el emtodo split separo las palabras por comas y klas guardo en una varibale palabras_separadas
        nueva_lista += palabras_separadas #agrego todsa laspalabras separadas en la lista nueva_lista 

    return nueva_lista #retorno la lista con las palabras separadas

#4.2
def stark_imprimir_indice_nombre(lista_heroes):
    # Llamo a mi función generar_indice_nombres para obtener el índice y lo guardo en una variable
    indice = generar_indice_nombres(lista_heroes)

    if indice:  # Verifico si el índice se generó correctamente
        print("-".join(indice))  # Si lo hizo, lo imprimo separando las palabras con guiones
    else:
        print("No se pudo generar un índice de nombres válidos")  # De lo contrario, imprime el mensaje de error

#5.1
def convertir_cm_a_mtrs(valor_cm):
    if type(valor_cm) in (int, float) and valor_cm >= 0: #verifico que valor_cm sea de tipo inf o float y que sea mayor o igual a 0
        metros = valor_cm / 100 #si cumple con estas condiciones, divido el valor por 100 para achicar las cifras y lo guardo en una variable metros
        return metros
    else:
        return -1
    
#5.2
def generar_separador(patron, largo, imprimir=True):
    if type(patron) == str and 1 <= len(patron) <= 2 and type(largo) == int: #verifico que patron se de tipo string y que tenga un minimo de 1 y max de 2 caracteres. Despues verifico que el largo sea un int
        if 1 <= largo <= 235:# si esto se verifica, ahora verifico que el largo esta dentro del largo de 1 y 235 caracteres
            separador = patron * largo #si lo esta, multiplico el patron por el largo de veces y lo guardo en una varaible separador
            if imprimir == True: #si imprimir es True
                print(separador) #imprimo el saparador
            return separador
    return print('N/A') #de lo contrario imprmimo N/A

#5.3
def generar_encabezado(titulo):
    if type(titulo) == str:  # Verifica si titulo es un string
        titulo = titulo.upper()  #convierto el titulo a letras mayusculas

        separador = generar_separador('*', len(titulo), False)# Llamo a mi funcion generar_separador para obtener el separador, le paso el patron, el largo del titulo y si es False en caso de que no deba imprimirse

        encabezado = f"{separador*20}\n {titulo} \n{separador*20}"#Genero el encabezado combinando el separador, el título y otro separador 

        return encabezado  #retorno el encabezado final
#5.4
def imprimir_ficha_heroe(lista_heroes):
   
    asignar_codigos = False  # Verificar si alguno de los héroes no tiene un código asignado

    for heroe in lista_heroes: #recorro la lista_heroes segun los heroes
        if 'codigo_heroe' not in heroe: #verifico que el codigo_heroe no este en el diccionario
            asignar_codigos = True #si encuentro un heroe sin codigo pongo en True

    # Si es necesario, asignar códigos a los héroes que no los tienen
    if asignar_codigos:
        primer_id = 1

        for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
            if 'codigo_heroe' not in heroe: #verfico que la clave codigo no este en el diccionario de heroes
                genero_heroe = heroe.get('genero')#si no esta, obtengo el valor del genero y lo guardo en una variable
                codigo = generar_codigo_heroe(primer_id, genero_heroe) #llamo a mi funcion generar_codigo_heroe y lo guardo en una variable codigo
                if len(codigo) == 10:#verifico que la longitud del codigo sea igual a 10
                    heroe['codigo_heroe'] = codigo #si lo es, agrego el codigo a mi lista y le asigno el valor
                    primer_id += 1

    separador = '*' * 95    # Crear el separador

    for heroe in lista_heroes: #recorro la lista_heroes segun cada heroe
        # Extraer los datos del héroe
        nombre_heroe = heroe.get('nombre', 'N/A')   
        iniciales = extraer_iniciales(nombre_heroe)
        identidad_secreta = heroe.get('identidad', 'N/A')
        consultora = heroe.get('empresa', 'N/A')
        codigo_heroe = heroe.get('codigo_heroe', 'N/A')

        altura = heroe.get('altura', 'N/A')
        peso = heroe.get('peso', 'N/A')
        fuerza = heroe.get('fuerza', 'N/A')

        color_ojos = heroe.get('color_ojos', 'N/A')
        color_pelo = heroe.get('color_pelo', 'N/A')

        # Imprimir la ficha del héroe
        print(separador)
        print('PRINCIPAL')
        print(separador)
        print('NOMBRE DEL HÉROE: {} ({})'.format(nombre_heroe, iniciales))
        print('IDENTIDAD SECRETA: {}'.format(identidad_secreta))
        print('CONSULTORA: {}'.format(consultora))
        print('CÓDIGO DE HÉROE : {}'.format(codigo_heroe))
        print(separador)
        print('FISICO')
        print(separador)
        print('ALTURA: {} Mtrs.'.format(altura))
        print('PESO: {} Kg.'.format(peso))
        print('FUERZA: {} N'.format(fuerza))
        print(separador)
        print('SEÑAS PARTICULARES')
        print(separador)
        print('COLOR DE OJOS: {}'.format(color_ojos))
        print('COLOR DE PELO: {}'.format(color_pelo))

#5.5
def stark_navegar_fichas(lista_heroes):
    if not lista_heroes: #verifico que la lista de heroes no este vacia
        print("No hay personajes para mostrar.")
        return

    ficha_actual = 0 #inicializo en 0 la variable ficha_actual para hacer seguimiento

    while True:
        heroe = lista_heroes[ficha_actual] #obtengo el heroe_actual y lo guardo en una varia<ble. Muestra el heroe que se va a ver en al ficha
        print("\nFicha del Héroe:") #muestro la ficha actual
     
        imprimir_ficha_heroe([heroe]) #llamo a mi funcion imprimir_ficha_heroe 

        print("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir") 
        opcion = input("Seleccione una opción: ").strip().lower()

        match opcion:
            case '1':
                ficha_actual = (ficha_actual - 1) % len(lista_heroes) # ajusto el valor de ficha_actual restando 1 y utilizando el operador % para asegurarse de que el índice esté dentro de los límites de la lista.
            case '2':
                ficha_actual = (ficha_actual + 1) % len(lista_heroes)# ajusta el valor de ficha_actual sumandio  1 y utilizando el operador % para asegurarse de que el índice esté dentro de los límites de la lista.
            case 's':
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")