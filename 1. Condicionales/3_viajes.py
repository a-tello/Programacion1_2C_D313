"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
a. Si es invierno: solo se viaja a Bariloche.
b. Si es verano: se viaja a Mar del plata y Cataratas.
c. Si es otoño: se viaja a todos los lugares.
d. Si es primavera: se viaja a todos los lugares menos Bariloche.
"""

destino = input('¿Cuál es su destino?: ')

print('1. Verano')
print('2. Otoño')
print('3. Invierno')
print('4. Primavera')

estacion = input('Seleccione la estación en la que desea viajar (1,2,3,4): ')

match estacion:
    case '1':
        if destino == 'Mar del plata' or destino == 'Cataratas':
            print('Se viaja')
        else:
            print('No se viaja')
    case '2':
            print('Se viaja')
    case '3':
        if destino == 'Bariloche':
            print('Se viaja')
        else:
            print('No se viaja')
    case '4':
        if destino == 'Bariloche':
            print('No se viaja')
        else:
            print('Se viaja')

