'''Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven'''

edades = [25, 36, 18, 23, 45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

persona_joven = None

for i in range(len(nombre)):
    if persona_joven == None or edades[persona_joven] > edades[i]:
        persona_joven = i
mensaje = f"la persona mas joven es {nombre[persona_joven]}"
mensaje += f"y tiene {edades[persona_joven]}"
print(mensaje)
