# Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(cantidad: int = 0) -> list|None:
    lista = []
    if cantidad < 0: 
        print('Cantidad de elementos no válida')
        return None
    
    for i in range(cantidad):
        num = int(input(f'Ingrese numero (pos {i + 1}): '))
        lista.append(num)
    
    return lista

# print(crear_array(5))




# ??????
# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.?



# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def promedio_lista(numeros: list) -> float:
    total = sum(numeros)
    cantidad = len(numeros)
    
    return total / cantidad



# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# print(f'El promedio de la lista es: {promedio_lista(lista_numeros)}')





# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def promedio_lista_pares(numeros: list) -> float:
    total = 0
    cantidad = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            total += numero
            cantidad += 1
    
    return total / cantidad

# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# print(f'El promedio de los numeros pares de la lista es: {promedio_lista_pares(lista_numeros)}')





# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def producto_lista(numeros: list) -> int|float:
    producto = 1
    
    for numero in numeros:
        producto *= numero
        
    return producto

# lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# print(f'El producto de los numeros de la lista es: {producto_lista(lista_numeros)}')





# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def maximo_lista(enteros: list) -> int:
    maximo = max(enteros)
    pos = enteros.index(maximo)
    
    return pos
    
# lista_numeros = [1,2,3,544,5,60,7,8,9,10]
# pos = maximo_lista(lista_numeros)
# print(f'El número de valor máximo se encuentra en la posicion: {pos} arr({pos + 1})')






# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
def pos_maximo_lista(enteros: list) -> None:
    maximo = max(enteros)
    posiciones = []
    
    for i, numero in enumerate(enteros):
        if numero == maximo:
            posiciones.append(i)
    
    print(f'El número de mayor valor se encuentra en la/s posicion/es: {posiciones}')
            
# lista_numeros = [1,2,3,544,544,60,7,8,9,10]
# pos_maximo_lista(lista_numeros)





# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# Una lista de nombres (lista_nombres).
# Un nombre a buscar en la lista (nombre_antiguo).
# Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.
def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:
    reemplazos = 0
    
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
    
    print(lista_nombres)
    return reemplazos
    

# lista_nombres = ['Juan', 'Alejandro', 'Ana', 'Sebastian', 'Iara', 'Alejandro']
# print(f'La cantidad de reemplazos fueron: {reemplazar_nombres(lista_nombres, "Alejandro", "Jose")}')








# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.
def interseccion(array_1: list, array_2: list) -> list:
    conjunto_1 = set(array_1)
    conjunto_2 = set(array_2)
    
    interseccion = list(conjunto_1 & conjunto_2)
    print(f'La interseccion entre {array_1} y {array_2} es {interseccion}')
    
# arr1 = [2,4,6,8,10]
# arr2 = [1,2,3,4,5]
# interseccion(arr1, arr2)





# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.
def union(array_1: list, array_2: list) -> list:
    conjunto_1 = set(array_1)
    conjunto_2 = set(array_2)
    
    union = list(conjunto_1 | conjunto_2)
    print(f'La interseccion entre {array_1} y {array_2} es {union}')
    
# arr1 = [2,4,6,8,10]
# arr2 = [1,2,3,4,5]
# union(arr1, arr2)





# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
def diferencia(array_1: list, array_2: list) -> list:
    conjunto_1 = set(array_1)
    conjunto_2 = set(array_2)
    
    diferencia = list(conjunto_1 - conjunto_2)
    print(f'La diferencia entre {array_1} y {array_2} es {diferencia}')

# arr1 = [2,4,6,8,10]
# arr2 = [1,2,3,4,5]
# diferencia(arr1, arr2)