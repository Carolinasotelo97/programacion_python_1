from data_stark import lista_personajes
from funciones import * 

bandera = True

while bandera:
    print("Elija qué operación quiere realizar: \n",
        "A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n",
        "B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n",
        "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n",
        "D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n",
        "E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\n",
        "F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n",
        "G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n",
        "H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n",
        "I. Listar todos los superhéroes agrupados por color de ojos.\n",
        "J. Listar todos los superhéroes agrupados por tipo de inteligencia\n",
        "X. Salir\n")
    respuesta = input(str("Ingrese una opción: ")) #parseo respuesta para que se ingrese solo las letras mayusculas

    match respuesta:
        case "A":
            mostrar_nb()
        case "B":
            mostrar_superheroeina_alta()
        case "C":
            mostrar_superheroes_altos()
        case "D":
            mostrar_superheroe_debil_m()
        case "E":
            mostrar_superheroe_debil_nb()
        case "F":
            promedio_fuerza_nb()
        case "G":
            contar_colores_ojos()
        case "H":
            contar_color_pelo()
        case "I":
            mostrar_superheroes_color_ojos()
        case "J":
            mostrar_superheroes_tipo_inteligencia()
        case "X":
            bandera = False