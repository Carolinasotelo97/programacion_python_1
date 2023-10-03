from data_stark import lista_personajes

bandera = True
fuerza_max = lista_personajes[0]
cantidad_personajes_masculinos = 0
total_peso_masculino = 0
cantidad_personajes_femeninas = 0
total_fuerza_femeninas = 0

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
            #recorro la lista de personajes y la imprimo
            for superheroe in lista_personajes:
                    print("Personaje: ", superheroe["nombre"], superheroe["identidad"], superheroe["empresa"], superheroe["altura"], superheroe["peso"], superheroe["genero"], superheroe["color_ojos"], superheroe["color_pelo"], superheroe["fuerza"], superheroe["inteligencia"], "\n------------------------------------------------------------------------------------------------------------------------------------------","\n")
        case "B":
            #recorro la lista de personajes por fuerza
            for fuerza in lista_personajes:
                if(int(fuerza["fuerza"]) > int(fuerza_max["fuerza"])): #parseo para que me convierta a int
                    fuerza_max = fuerza
            #imprimo la lista segun la identidad y peso con mayor fuerza
            print("******* PERSONAJE CON MAS FUERZA *******")
            print("Identidad:{0}\nFuerza:{1}\nPeso:{2}\n" .format(fuerza_max["identidad"], fuerza_max["fuerza"], fuerza_max["peso"]))
        case "C":
            #inicializo
            altura_min = lista_personajes[0]
            #recorro la lista de personajes buscando la altura minima
            for alturas in lista_personajes:
                if(float(alturas["altura"]) < float(altura_min["altura"])): #parseo para que me convierta a float
                    altura_min = alturas
            #imprimo el personaje mas bajo
            print("******* PERSONAJE MAS BAJO *******")
            print("Identidad:{0}\nNombre:{1}\nAltura:{2}\n" .format(altura_min["identidad"], altura_min["nombre"], altura_min["altura"]))
        case "D":
            #recorro la lista de personajes por pesos
            for pesos in lista_personajes:
                #inicializo
                genero = pesos["genero"]
                cantidad_personajes_masculinos+= 1 #cuento los personajes que son masculinos
                float(pesos["peso"]) #parseo el peso a numero float
                total_peso_masculino += float(pesos["peso"])
            
            #verifico que el personajes sea masculino
            if genero == "M":
                total_peso_masculino += float(pesos["peso"])
                cantidad_personajes_masculinos +=1
            
            #verifico que haya personajes masculinos e imprimo su peso promedio
            if cantidad_personajes_masculinos > 0:
                peso_promedio_masculino = total_peso_masculino / cantidad_personajes_masculinos
                print("******* PESO PROMEDIO SUPERHEROES MASCULINOS *******")
                print("Peso promedio:", peso_promedio_masculino, "\n")
            else:
                print("No hay superhéroes masculinos en la lista.")
        case "E":
            print("******* SUPERHEROES CON MAS FUERZA DEL PROMEDIO DE FUERZA DE MUJERES *******")
            #recorro la lista de personajes
            for superheroes in lista_personajes:
                #verifico si el personaje es femenino y lo incremento por fuerza
                if superheroes["genero"] == "F":
                    total_fuerza_femeninas += int(superheroes["fuerza"])#parseo la fuerza a int
                    cantidad_personajes_femeninas += 1

            # Verifico si hay superhéroes mujeres en la lista y muestro el promedio de fuerza
            if cantidad_personajes_femeninas > 0:
                fuerza_promedio_femenina = total_fuerza_femeninas / cantidad_personajes_femeninas
            else:
                fuerza_promedio_femenina = 0    

            # Recorro la lista de superhéroes y muestro nombre y peso de los que tienen fuerza superior al promedio de mujeres
            for superheroes in lista_personajes:
                if int(superheroes["fuerza"]) > fuerza_promedio_femenina:
                    print("Nombre:{0}\nPeso:{1}\n-----------------------" .format(superheroes["nombre"], superheroes["peso"]))
        case "X":
            bandera = False
            print("Adios.")
        case _:
            print("Ingrese una opción válida.\n")