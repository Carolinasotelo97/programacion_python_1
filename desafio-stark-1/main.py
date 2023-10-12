from data_stark import lista_personajes

bandera = True #inicializo bandera en True para controlar el bucle While 
fuerza_max = lista_personajes[0] #inicializo la variable fuerza_max con el primer elemento de la lista_personajes para indicar que es el superheroe con mas fuerza hasta que encuentre otro
cantidad_personajes_masculinos = 0  #inicializo esta variable en 0 para llevar la cuenta de la cantidad de masculinos
total_peso_masculino = 0 #inciailizo esta variable en 0 para llevar la cuenta del total de pesos masculinos
cantidad_personajes_femeninas = 0 #inicializo esta variable en 0 para llevar la cuenta de la cantidad de femeninas
total_fuerza_femeninas = 0 #inciailizo esta variable en 0 para llevar la cuenta del total de fuerza femenina

while bandera:
    print("Elija qué operación quiere realizar: \n",
        "A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe\n",
        "B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)\n",
        "C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)\n",
        "D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)\n",
        "E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) cuya fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\n",
        "X. Salir")
    respuesta = input(str("Ingrese una opción: ")) #parseo respuesta para que se ingrese solo las letras mayusculas

    match respuesta:
        case "A":
            print("*********************************       LISTA DE PERSONAJES       *********************************")
            
            for superheroe in lista_personajes: #recorro la lista_personajes segun cada elemento
                    print("Personaje: ", superheroe["nombre"], superheroe["identidad"], superheroe["empresa"], superheroe["altura"], superheroe["peso"], superheroe["genero"], superheroe["color_ojos"], superheroe["color_pelo"], superheroe["fuerza"], superheroe["inteligencia"], "\n------------------------------------------------------------------------------------------------------------------------------------------","\n")
                    #imprimo valor de las claves que le paso 
        case "B":
            #recorro la lista de personajes por fuerza
            for fuerza in lista_personajes: #recorro la lista_personajes segun cada elemento 
                if(int(fuerza["fuerza"]) > int(fuerza_max["fuerza"])): #verifico que la fuerza del supereheroe actual es mayor que la fuerza max encontrada 
                    fuerza_max = fuerza #si la fuerza actual es mayor a la max, actualizo la varibale fuerza_max co la nueva fuerza encontrada
            
            print("******* PERSONAJE CON MAS FUERZA *******")
            print("Identidad:{0}\nFuerza:{1}\nPeso:{2}\n" .format(fuerza_max["identidad"], fuerza_max["fuerza"], fuerza_max["peso"]))
        case "C":
            altura_min = lista_personajes[0] #inicializo la variable altura_min con el primer elemento de la lista_personajes para indicar que es el superheroe con altura_min hasta el momento
            
            for alturas in lista_personajes:#recorro la lista de personajes buscando la altura minima
                if(float(alturas["altura"]) < float(altura_min["altura"])): #verifico que la altura actual sea menor que la altura_min encontrada
                    altura_min = alturas #si lo es, actualizo la variable altura_min con la nueva altura encontrada
            #imprimo el personaje mas bajo
            print("******* PERSONAJE MAS BAJO *******")
            print("Identidad:{0}\nNombre:{1}\nAltura:{2}\n" .format(altura_min["identidad"], altura_min["nombre"], altura_min["altura"]))
        case "D":
            for pesos in lista_personajes: #recorro la lista de personajes por pesos
                genero = pesos["genero"] #obtengo el genero del superheroe actual y lo guardo en una variable genero
                cantidad_personajes_masculinos+= 1 #aumento en 1 la cantidad de personajes masculinos cada vez que itero en la lista
                float(pesos["peso"]) #parseo el peso a numero float
                total_peso_masculino += float(pesos["peso"]) #sumo el peso actual al contador total_peso_masculino
            
            if genero == "M": #verifico que el personajes sea masculino
                total_peso_masculino += float(pesos["peso"]) #sumo el peso actual al contador total_peso_masculino
                cantidad_personajes_masculinos +=1 #aumento en 1 la cantidad de personajes masculinos
            
            
            if cantidad_personajes_masculinos > 0:#verifico que haya personajes masculinos
                peso_promedio_masculino = total_peso_masculino / cantidad_personajes_masculinos #guardo en la variable peso_promedio_masculino la division del total_perso y cantidad_personajes_masculinos para obtener el promedio
                print("******* PESO PROMEDIO SUPERHEROES MASCULINOS *******")
                print("Peso promedio:", peso_promedio_masculino, "\n")
            else:
                print("No hay superhéroes masculinos en la lista.")
        case "E":
            print("******* SUPERHEROES CON MAS FUERZA DEL PROMEDIO DE FUERZA DE MUJERES *******")
            for superheroes in lista_personajes: #recorro la lista de personajes segun cada elemento
                if superheroes["genero"] == "F": #verifico si el personaje es genero femenino 
                    total_fuerza_femeninas += int(superheroes["fuerza"])#incremento la fuerza en mi variable total_fuerza_femenina para acumular la fuerza
                    cantidad_personajes_femeninas += 1 #incremento en uno la cantidad_personajes_femininos para saber cuantos encontre 

            if cantidad_personajes_femeninas > 0: # Verifico si hay superhéroes mujeres en la lista
                fuerza_promedio_femenina = total_fuerza_femeninas / cantidad_personajes_femeninas #si los hay, guardo en la variable fuerza_promedio_femenina la division del total y cantidad de mujeres para obtener el promedio
            else:
                fuerza_promedio_femenina = 0    

            for superheroes in lista_personajes:# Recorro la lista de superhéroes
                if int(superheroes["fuerza"]) > fuerza_promedio_femenina: #verifico si la fuerza femenina actual es mayor a la fuerza promedio obtenida<
                    print("Nombre:{0}\nPeso:{1}\n-----------------------" .format(superheroes["nombre"], superheroes["peso"]))
        case "X":
            bandera = False #inicializo en False para indicar que se termina el bucle 
            print("Adios.")
        case _: #en caso de opcion no valida
            print("Ingrese una opción válida.\n")