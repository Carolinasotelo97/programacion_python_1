from data_stark import lista_personajes
from funciones import*

def imprimir_menu():
    print("\n            MENU PRINCIPAL      \n",
        "1 - Imprimir la lista de nombres junto con sus iniciales\n",
        "2 - Generar códigos de héroes\n",
        "3 - Normalizar datos\n",
        "4 - Imprimir índice de nombres\n",
        "5 - Navegar fichas\n",
        "S - Salir\n")

def stark_menu_principal():
    imprimir_menu()  # Llamar a la función para imprimir el menú
    opcion = input("Ingrese una opción: ").strip().upper()
    return opcion

def stark_marvel_app_3(lista_heroes):
    while True:
        opcion = stark_menu_principal()  # Obtener la opción del menú principal

        match opcion:
            case '1':
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            case '2':
                stark_generar_codigos_heroes(lista_heroes)
            case '3':
                stark_normalizar_datos(lista_heroes)
            case '4':
                stark_imprimir_indice_nombre(lista_heroes)
            case '5':
                stark_navegar_fichas(lista_heroes)
            case 'S':
                print("Saliendo del programa...")
                return
            case _:
                print("Opción incorrecta. Por favor, seleccione una opción válida.")