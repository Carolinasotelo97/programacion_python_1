from funciones import*

#5.1
def imprimir_menu(opciones):
    
    for opcion in opciones:
        print(opcion)


#5.2                
def validar_entero(cadena): #le paso un unico argumento que es lo que quiero verificar 
    
    return cadena.isdigit() #uso isdigit para saber si me funcion devuelve True en caso de que sea una cadena de numeros, y de lo contrario devolverá false

#5.3
def stark_menu_principal():

    opciones = [
        print("Elija qué operación quiere realizar: \n",
            "1. Normalizar datos\n",
            "2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n",
            "3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n",
            "4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n",
            "5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n",
            "6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n",
            "7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n",
            "8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n",
            "9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n",
            "10. Listar todos los superhéroes agrupados por color de ojos.\n",
            "11. Listar todos los superhéroes agrupados por tipo de inteligencia\n",
            "0. Salir\n")]   
    
    respuesta = input("Ingrese una opción: ")

    if respuesta.isdigit():
        opcion = int(respuesta)
        if 0 <= opcion <= 11:
            return opcion
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 11.")
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 11.")

#6
# 6. Función principal de la aplicación Stark Marvel
def stark_marvel_app(lista_personajes):
    datos_normalizados = False
    opcion_uno = False
    opcion_ingresada = True

    while opcion_ingresada:
        respuestas = stark_menu_principal()

        if not opcion_uno and respuestas != 1:
            print("Primero debes seleccionar la opción 1 para normalizar los datos.")
            continue
       
        match respuestas:
            case 1:
                if not datos_normalizados:
                    datos_normalizados = stark_normalizar_datos(lista_personajes)
                    opcion_uno = True
                else:
                    print("Los datos ya fueron normalizados.")
            case 2:
                mostrar_heroe_nb(lista_personajes)
            case 3:
                mostrar_superheroeina_alta()
            case 4:
                mostrar_superheroes_altos()
            case 5:
                mostrar_superheroe_debil_m()
            case 6:
                mostrar_superheroe_debil_nb()
            case 7:
                promedio_fuerza_nb()
            case 8:
                contar_colores_ojos()
            case 9:
                contar_color_pelo()
            case 10:
                mostrar_superheroes_color_ojos()
            case 11:
                mostrar_superheroes_tipo_inteligencia()
            case 0:
                print("¡Adiós!")
                opcion_ingresada = False
            case _:
                if not opcion_uno:
                    print("Primero debes seleccionar la opción 1 para normalizar los datos.")
                else:
                    print("Opción no válida. Por favor, ingrese una opción válida.")
