# 📌 Desafío: Menú de Opciones con Listas y Funciones
# Desarrollar un programa en Python que presente un menú de opciones donde el usuario pueda realizar distintas operaciones con un conjunto de números.

# 🔹 Opciones del Menú:
#  1️⃣ Ingresar datos: Permitir al usuario ingresar 10 números enteros en el rango de -1000 a 1000.
#  2️⃣ Cantidad de positivos y negativos: Mostrar cuántos números ingresados son positivos y cuántos son negativos.
#  3️⃣ Suma de los números pares: Calcular y mostrar la sumatoria de los números pares.
#  4️⃣ Mayor número impar: Identificar y mostrar el mayor número impar ingresado.
#  5️⃣ Listar los números ingresados: Mostrar todos los números en el orden en que fueron ingresados.
#  6️⃣ Listar los números pares: Mostrar únicamente los números pares de la lista.
#  7️⃣ Listar los números en posiciones impares: Mostrar los números que se encuentran en posiciones impares dentro de la lista.
#  8️⃣ Salir del programa.
# 🔹 Condiciones:
#  ✔️ El usuario debe ingresar los números antes de acceder a las opciones 2 a 7.
#  ✔️ El programa debe estar estructurado en funciones, siguiendo el paradigma de programación funcional:
# Funciones específicas: Para operaciones como determinar si un número es positivo, negativo o par.
# Funciones generales: Para listar elementos o calcular sumatorias.
# 🔹 Estructura del Código:
#  📌 El programa debe estar organizado en módulos:
# Especificas.py: Contendrá las funciones específicas.
# Array_Generales.py: Contendrá las funciones generales.
# Las funciones de entrada de datos deben importarse desde el módulo   .
# 🔹 Consejo:
#  ✅ Desarrollar y probar primero cada función individualmente antes de organizarlas en módulos.

import os
import Array_Generales as Arr

def mostrar_menu():
    print(f"""{"-"*20}LISTAS{"-"*20}
    1. Ingresar datos
    2. Cantidad de positivos y negativos
    3. Suma de los números pares
    4. Mayor número impar
    5. Listar números ingresados
    6. Listar números pares
    7. Listar números en posiciones impares
    8. Salir
        """)
    

cargados = False
numeros = []

while True:
    mostrar_menu()
    opcion = int(input('Seleccione una opción (1 a 8): '))
    
    if 1 < opcion < 8 and not cargados: 
        os.system('cls')
        print('Debe cargar los datos antes de seleccionar otra opción\n')
        continue
    
    match opcion:
        case 1:
            os.system('cls')
            numeros = Arr.crear_array(10)
            cargados = True
        case 2:
            os.system('cls')
            positivos, negativos = Arr.positivos_negativos_array(numeros)
            print(f'La cantidad de números positivos es: {positivos}\nLa cantidad de números negativos es: {negativos}')
            input('\n\n\nPresione enter para volver al menu...')
        case 3:
            os.system('cls')
            suma = Arr.suma_pares(numeros)
            print(f'La suma de los números pares es: {suma}')
            input('\n\n\nPresione enter para volver al menu...')
        case 4:
            os.system('cls')
            impar = Arr.mayor_numero_impar(numeros)
            print(f'El mayor número impar es: {impar}') if impar else print('No hay números impares')
            input('\n\n\nPresione enter para volver al menu...')
        case 5:
            os.system('cls')
            Arr.mostrar_array(numeros)
            input('\n\n\nPresione enter para volver al menu...')
        case 6:
            os.system('cls')
            Arr.mostrar_pares_array(numeros)
            input('\n\n\nPresione enter para volver al menu...')
        case 7:
            os.system('cls')
            Arr.mostrar_posiciones_impares_array(numeros)
            input('\n\n\nPresione enter para volver al menu...')
        case 8:
            break
        case _: 
            os.system('cls')
            print('\nOpción incorrecta. Debe seleccionar una opcion entre 1 y 8\n\n')
    
    
