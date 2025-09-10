# # # # # # # # # # # # # # # # # # # # # # # 
#                                           #
#  Uncomment the lines to execute the code  #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # # 

# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def enter_int():
    num = int(input("Enter a integer: "))
    return num

# print(enter_int())



# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def enter_float():
    num = float(input('Enter a float number: '))
    return num

# print(enter_float())




# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def enter_str():
    string = input('Enter a string of characters: ')
    return string
    
# print(enter_str())
    
    
    
    
# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
def rectangle_area(base, height):
    area = base * height
    return area

# area = rectangle_area(5, 8)
# print(f'The area of rectangle is: {area}')
    
    
    

# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def circle_area(radius):
    PI = 3.14
    area = PI * radius ** 2
    return area

# area = circle_area(5)
# print(f'The area of circle is: {area}')




# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def even_odd(num):
    print(f'{num} is an even number') if num % 2 == 0 else print(f'{num} is an odd number')
    
# even_odd(10)
    



# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def is_even(num):
    return True if num % 2 == 0 else False

# print(is_even(55))





# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def greater_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

# print(f'The greater number is: {greater_of_three(100, 32, 15)}')




# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def power_of_number(base, exponent):
    result = base ** exponent
    return result

# base = 7
# exponent = 3
# print(f'{base} to the power of {exponent} is: {power_of_number(base,exponent)}')




# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def is_primer_number(num):
    if num == 1: return False
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False
    return True

# print(is_primer_number(11))




# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
def prime_numbers(num):
    prime_numbers = 0
    for i in range(1, num+1):
        if is_primer_number(i):
            prime_numbers += 1
            print(i,end=', ')
            
    print('')
    return prime_numbers

# n = 13
# print(f'There are {prime_numbers(n)} prime numbers between 1 and {n}')




# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
def multiplication_table(num, start=1, end=10):
    for i in range(start, end + 1):
        print(f'{num} X {i} = {num * i}')
        
# multiplication_table(5, 1, 5)




# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
def enter_int_v2():
    num = int(input("Enter a integer: "))
    return num

# print(enter_int_v2())



def enter_float_v2():
    num = float(input('Enter a float number: '))
    return num

# print(enter_float_v2())



def enter_str_v2():
    string = input('Enter a string of characters: ')
    return string
    
# print(enter_str_v2())