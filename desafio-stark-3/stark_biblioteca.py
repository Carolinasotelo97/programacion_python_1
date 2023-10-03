from data_stark import lista_personajes

def mostrar_nb():
    personajes_nb = False # inicializo la varibale en false

    for superheroe in lista_personajes:
        if str(superheroe["genero"]) == 'NB':
            personajes_nb = True
            print("Personaje: ", superheroe["nombre"], superheroe["identidad"], superheroe["empresa"], superheroe["altura"], superheroe["peso"], superheroe["genero"], superheroe["color_ojos"], superheroe["color_pelo"], superheroe["fuerza"], superheroe["inteligencia"], "\n------------------------------------------------------------------------------------------------------------------------------------------","\n")
    
    if personajes_nb == False:
        print("No se encontraron superheroes no binarios")

def mostrar_superheroeina_alta():
    altura_max_f = lista_personajes[0] #inicializo con la primer superheroina mujer de la lista

    for alturas in lista_personajes: #recorro la lista segun la altura 
        if alturas["genero"] == "F" and float(alturas["altura"]) > float(altura_max_f["altura"]): #verifico si el superheroe actual es F y si la altura actual es mayor a la altura maxima registrada
            altura_max_f = alturas  #el nuevo dato lo guardo en la variable alturas 
    
    if altura_max_f["genero"] == "F": #verifico que el dato obtenido sea F y si es asi, imprime los datos
        print("******* SUPERHEROINA MAS ALTA *******")
        print("Identidad:{0}\nNombre:{1}\nAltura:{2}\nGenero:{3}" .format(altura_max_f["identidad"], altura_max_f["nombre"], altura_max_f["altura"], altura_max_f["genero"]))
    else:
        print("No hay superheroinas")

def mostrar_superheroes_altos():
    altura_max_m = lista_personajes[0] #inicializo con la primer superheroes M de la lista

    for alturas in lista_personajes: #recorro la lista segun la altura 
        if alturas["genero"] == "M" and float(alturas["altura"]) > float(altura_max_m["altura"]): #verifico si el superheroe actual es M y si la altura actual es mayor a la altura maxima registrada
            altura_max_m = alturas  #el nuevo dato lo guardo en la variable alturas 
    
    if altura_max_m["genero"] == "M": #verifico que el dato obtenido sea M y si es asi, imprime los datos
        print("******* SUPERHEROE MAS ALTO *******")
        print("Identidad:{0}\nNombre:{1}\nAltura:{2}\nGenero:{3}" .format(altura_max_m["identidad"], altura_max_m["nombre"], altura_max_m["altura"], altura_max_m["genero"]))
    else:
        print("No hay superheroes")

def mostrar_superheroe_debil_m():
    fuerza_min_m = lista_personajes[0] #incializo con el primer superheroe de la lista

    for fuerzas in lista_personajes: #recorro la lista segun la fuerza
        if fuerzas["genero"] == "M" and int(fuerzas["fuerza"]) < int(fuerza_min_m["fuerza"]):
            fuerza_min_m = fuerzas

    if fuerza_min_m["genero"] == "M":
        print("******* SUPERHEROE MAS DEBIL *******")
        print("Identidad:{0}\nNombre:{1}\nFuerza:{2}\nGenero:{3}" .format(fuerza_min_m["identidad"], fuerza_min_m["nombre"], fuerza_min_m["fuerza"], fuerza_min_m["genero"]))
    else:
        print("No hay superheroes")

def mostrar_superheroe_debil_nb():
    fuerza_min_nb = None  # Inicializo con None para encontrar el superheroe mas debil NB

    #recorro toda la lista de personajes segun fuerza
    for fuerza in lista_personajes: 
        if fuerza["genero"] == "NB": #verifico si hay un superheroe NB
            if fuerza_min_nb is None or int(fuerza["fuerza"]) < int(fuerza_min_nb["fuerza"]): #verifico que no haya ningun NB en lista y comparo la fuerza del superheroe actual con la del nb mas debil 
                fuerza_min_nb = fuerza #me guardo el dato nuevo y actualizo

    if fuerza_min_nb is not None: #verifico si no es None para encontrar al menos un superheroe NB
        print("******* SUPERHEROE NO BINARIO MÁS DÉBIL *******") #imprimo
        print("Identidad: {}\nNombre: {}\nFuerza: {}\nGenero: {}".format(
            fuerza_min_nb["identidad"],
            fuerza_min_nb["nombre"],
            fuerza_min_nb["fuerza"],
            fuerza_min_nb["genero"]
        ))
    else:
        print("No hay superhéroes no binarios en la lista.")

def promedio_fuerza_nb():
    cantidad_personajes_nb = 0
    total_fuerza_nb = 0
    
    for fuerzas in lista_personajes:
        if fuerzas["genero"] == "NB":
            cantidad_personajes_nb += 1
            total_fuerza_nb += int(fuerzas["fuerza"])
    
    if cantidad_personajes_nb > 0:
        fuerza_promedio_nb = total_fuerza_nb / cantidad_personajes_nb
        print("******* FUERZA PROMEDIO SUPERHEROES NO BINARIOS *******")
        print("Fuerza promedio:", fuerza_promedio_nb)
    else:
        print("No hay superhéroes no binarios en la lista.")

def contar_colores_ojos():
    cantidad_color_ojos = {}  #Creo un diccionario vacio para listar la cantidad de cada color de ojos

    #recorror todos los colores de ojos en la lista
    for ojos in lista_personajes:
        color_ojos = ojos.get("color_ojos")  # Obtengo el color 
        cantidad_actual_ojos = cantidad_color_ojos.get(color_ojos, 0)
        cantidad_color_ojos[color_ojos] = cantidad_actual_ojos + 1 #obtengo la cantidad actual de ese color de ojos en el diccionario e incremento la cantidad para ese color de ojos en 1. Pongo 0 como valor predeterminado si el color no esta cargado

    print("******* CANTIDAD DE SUPERHEROES POR COLOR DE OJOS **********") #imprimo
    for color, cantidad in cantidad_color_ojos.items():
        print("{}: {}" .format(color, cantidad))

def contar_color_pelo():
    cantidad_color_pelo= {}

    for pelo in lista_personajes:
        colores_pelo = pelo.get("color_pelo", "Desconocido")# obtengo el color y en la segunda parte coloco desconocido para aquellos que no definan el color.
        cantidad_actual_pelo = cantidad_color_pelo.get(colores_pelo, 0)
        cantidad_color_pelo[colores_pelo] = cantidad_actual_pelo + 1

    print("********* CANTIDAD DE PERSONAJES POR COLOR DE PELO ***********")
    for color, cantidad in cantidad_color_pelo.items():
        print("{} : {}" .format(color, cantidad))

def mostrar_superheroes_color_ojos():
    superheroes_color_ojos = {} #creo un diccionario vacio para listar todos los nombres por grupo de color

    for heroe in lista_personajes: #recorro la lista de personajes segun cada personaje
        color_ojos = heroe["color_ojos"]  # Obtengo el color 
        if color_ojos in superheroes_color_ojos:
            superheroes_color_ojos[color_ojos].append(heroe["nombre"]) #agrego el nombre del superheroe si el color ya existe
        else:
            superheroes_color_ojos[color_ojos] = [heroe["nombre"]] #si el nuevo color no existe, agrego un nuevo color y nombre en la lista
    
    print("************ LISTA DE SUPERHEROES POR COLOR DE OJOS ************\n --------------------------------------------------------------\n")
    for color_ojos, personajes in superheroes_color_ojos.items(): #recorro la lista de ojos y personajes segun los items de mi diccionario
        print("Color de ojos: {}" .format(color_ojos)) #imprimo el color
        for personaje in personajes:
            print("  - {}" .format(personaje)) #imprimo el personaje

def mostrar_superheroes_tipo_inteligencia():
    inteligencia_superheroes = {} #creo un diccionario vacio para listar todos los nombres por tipo de inteligencia

    for superheroe in lista_personajes: #recorro la lista de personajes segun cada personaje
        tipo_inteligencia = superheroe["inteligencia"]  # Obtengo el color 
        if tipo_inteligencia in inteligencia_superheroes:
            inteligencia_superheroes[tipo_inteligencia].append(superheroe["nombre"]) #agrego el nombre del superheroe si la integligencia ya existe
        else:
            inteligencia_superheroes[tipo_inteligencia] = [superheroe["nombre"]] #si la inteligencia no existe, agrego un nuevo tipo y nombre en la lista
    
    print("************ LISTA DE SUPERHEROES POR TIPOS DE INTELIGENCIA ************\n --------------------------------------------------------------")
    for tipo_inteligencia, personajes in inteligencia_superheroes.items(): #recorro la lista de inteligencia y personajes segun los items de mi diccionario
        print("Tipo de Inteligencia: {}" .format(tipo_inteligencia)) #imprimo el tipo
        for personaje in personajes:
            print("  - {}" .format(personaje)) #imprimo el personaje
            
def mostrar_nb():
    personajes_nb = False # inicializo la varibale en false

    for superheroe in lista_personajes:
        if str(superheroe["genero"]) == 'NB':
            personajes_nb = True
            print("Personaje: ", superheroe["nombre"], superheroe["identidad"], superheroe["empresa"], superheroe["altura"], superheroe["peso"], superheroe["genero"], superheroe["color_ojos"], superheroe["color_pelo"], superheroe["fuerza"], superheroe["inteligencia"], "\n------------------------------------------------------------------------------------------------------------------------------------------","\n")
    
    if personajes_nb == False:
        print("No se encontraron superheroes no binarios")

def mostrar_superheroeina_alta():
    altura_max_f = lista_personajes[0] #inicializo con la primer superheroina mujer de la lista

    for alturas in lista_personajes: #recorro la lista segun la altura 
        if alturas["genero"] == "F" and float(alturas["altura"]) > float(altura_max_f["altura"]): #verifico si el superheroe actual es F y si la altura actual es mayor a la altura maxima registrada
            altura_max_f = alturas  #el nuevo dato lo guardo en la variable alturas 
    
    if altura_max_f["genero"] == "F": #verifico que el dato obtenido sea F y si es asi, imprime los datos
        print("******* SUPERHEROINA MAS ALTA *******")
        print("Identidad:{0}\nNombre:{1}\nAltura:{2}\nGenero:{3}" .format(altura_max_f["identidad"], altura_max_f["nombre"], altura_max_f["altura"], altura_max_f["genero"]))
    else:
        print("No hay superheroinas")

def mostrar_superheroes_altos():
    altura_max_m = lista_personajes[0] #inicializo con la primer superheroes M de la lista

    for alturas in lista_personajes: #recorro la lista segun la altura 
        if alturas["genero"] == "M" and float(alturas["altura"]) > float(altura_max_m["altura"]): #verifico si el superheroe actual es M y si la altura actual es mayor a la altura maxima registrada
            altura_max_m = alturas  #el nuevo dato lo guardo en la variable alturas 
    
    if altura_max_m["genero"] == "M": #verifico que el dato obtenido sea M y si es asi, imprime los datos
        print("******* SUPERHEROE MAS ALTO *******")
        print("Identidad:{0}\nNombre:{1}\nAltura:{2}\nGenero:{3}" .format(altura_max_m["identidad"], altura_max_m["nombre"], altura_max_m["altura"], altura_max_m["genero"]))
    else:
        print("No hay superheroes")

def mostrar_superheroe_debil_m():
    fuerza_min_m = lista_personajes[0] #incializo con el primer superheroe de la lista

    for fuerzas in lista_personajes: #recorro la lista segun la fuerza
        if fuerzas["genero"] == "M" and int(fuerzas["fuerza"]) < int(fuerza_min_m["fuerza"]):
            fuerza_min_m = fuerzas

    if fuerza_min_m["genero"] == "M":
        print("******* SUPERHEROE MAS DEBIL *******")
        print("Identidad:{0}\nNombre:{1}\nFuerza:{2}\nGenero:{3}" .format(fuerza_min_m["identidad"], fuerza_min_m["nombre"], fuerza_min_m["fuerza"], fuerza_min_m["genero"]))
    else:
        print("No hay superheroes")

def mostrar_superheroe_debil_nb():
    fuerza_min_nb = None  # Inicializo con None para encontrar el superheroe mas debil NB

    #recorro toda la lista de personajes segun fuerza
    for fuerza in lista_personajes: 
        if fuerza["genero"] == "NB": #verifico si hay un superheroe NB
            if fuerza_min_nb is None or int(fuerza["fuerza"]) < int(fuerza_min_nb["fuerza"]): #verifico que no haya ningun NB en lista y comparo la fuerza del superheroe actual con la del nb mas debil 
                fuerza_min_nb = fuerza #me guardo el dato nuevo y actualizo

    if fuerza_min_nb is not None: #verifico si no es None para encontrar al menos un superheroe NB
        print("******* SUPERHEROE NO BINARIO MÁS DÉBIL *******") #imprimo
        print("Identidad: {}\nNombre: {}\nFuerza: {}\nGenero: {}".format(
            fuerza_min_nb["identidad"],
            fuerza_min_nb["nombre"],
            fuerza_min_nb["fuerza"],
            fuerza_min_nb["genero"]
        ))
    else:
        print("No hay superhéroes no binarios en la lista.")

def promedio_fuerza_nb():
    cantidad_personajes_nb = 0
    total_fuerza_nb = 0
    
    for fuerzas in lista_personajes:
        if fuerzas["genero"] == "NB":
            cantidad_personajes_nb += 1
            total_fuerza_nb += int(fuerzas["fuerza"])
    
    if cantidad_personajes_nb > 0:
        fuerza_promedio_nb = total_fuerza_nb / cantidad_personajes_nb
        print("******* FUERZA PROMEDIO SUPERHEROES NO BINARIOS *******")
        print("Fuerza promedio:", fuerza_promedio_nb)
    else:
        print("No hay superhéroes no binarios en la lista.")

def contar_colores_ojos():
    cantidad_color_ojos = {}  #Creo un diccionario vacio para listar la cantidad de cada color de ojos

    #recorror todos los colores de ojos en la lista
    for ojos in lista_personajes:
        color_ojos = ojos.get("color_ojos")  # Obtengo el color 
        cantidad_actual_ojos = cantidad_color_ojos.get(color_ojos, 0)
        cantidad_color_ojos[color_ojos] = cantidad_actual_ojos + 1 #obtengo la cantidad actual de ese color de ojos en el diccionario e incremento la cantidad para ese color de ojos en 1. Pongo 0 como valor predeterminado si el color no esta cargado

    print("******* CANTIDAD DE SUPERHEROES POR COLOR DE OJOS **********") #imprimo
    for color, cantidad in cantidad_color_ojos.items():
        print("{}: {}" .format(color, cantidad))

def contar_color_pelo():
    cantidad_color_pelo= {}

    for pelo in lista_personajes:
        colores_pelo = pelo.get("color_pelo", "Desconocido")# obtengo el color y en la segunda parte coloco desconocido para aquellos que no definan el color.
        cantidad_actual_pelo = cantidad_color_pelo.get(colores_pelo, 0)
        cantidad_color_pelo[colores_pelo] = cantidad_actual_pelo + 1

    print("********* CANTIDAD DE PERSONAJES POR COLOR DE PELO ***********")
    for color, cantidad in cantidad_color_pelo.items():
        print("{} : {}" .format(color, cantidad))

def mostrar_superheroes_color_ojos():
    superheroes_color_ojos = {} #creo un diccionario vacio para listar todos los nombres por grupo de color

    for heroe in lista_personajes: #recorro la lista de personajes segun cada personaje
        color_ojos = heroe["color_ojos"]  # Obtengo el color 
        if color_ojos in superheroes_color_ojos:
            superheroes_color_ojos[color_ojos].append(heroe["nombre"]) #agrego el nombre del superheroe si el color ya existe
        else:
            superheroes_color_ojos[color_ojos] = [heroe["nombre"]] #si el nuevo color no existe, agrego un nuevo color y nombre en la lista
    
    print("************ LISTA DE SUPERHEROES POR COLOR DE OJOS ************\n --------------------------------------------------------------\n")
    for color_ojos, personajes in superheroes_color_ojos.items(): #recorro la lista de ojos y personajes segun los items de mi diccionario
        print("Color de ojos: {}" .format(color_ojos)) #imprimo el color
        for personaje in personajes:
            print("  - {}" .format(personaje)) #imprimo el personaje

def mostrar_superheroes_tipo_inteligencia():
    inteligencia_superheroes = {} #creo un diccionario vacio para listar todos los nombres por tipo de inteligencia

    for superheroe in lista_personajes: #recorro la lista de personajes segun cada personaje
        tipo_inteligencia = superheroe["inteligencia"]  # Obtengo el color 
        if tipo_inteligencia in inteligencia_superheroes:
            inteligencia_superheroes[tipo_inteligencia].append(superheroe["nombre"]) #agrego el nombre del superheroe si la integligencia ya existe
        else:
            inteligencia_superheroes[tipo_inteligencia] = [superheroe["nombre"]] #si la inteligencia no existe, agrego un nuevo tipo y nombre en la lista
    
    print("************ LISTA DE SUPERHEROES POR TIPOS DE INTELIGENCIA ************\n --------------------------------------------------------------")
    for tipo_inteligencia, personajes in inteligencia_superheroes.items(): #recorro la lista de inteligencia y personajes segun los items de mi diccionario
        print("Tipo de Inteligencia: {}" .format(tipo_inteligencia)) #imprimo el tipo
        for personaje in personajes:
            print("  - {}" .format(personaje)) #imprimo el personaje