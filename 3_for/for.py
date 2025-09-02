# # # # # # # # # # # # # # # # # # # # # # # 
#                                           #
#  Uncomment the lines to execute the code  #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # # 

# Mostrar los números ascendentes desde el 1 al 10

# for i in range(10):
#     print(i+1)


# Mostrar los números descendentes desde el 10 al 1

# for i in range(10, 0, -1):
#     print(i)
    
    
    
# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# number = int(input('Enter a number: '))

# for i in range(number+1):
#     print(i, end=', ')
    
    
# Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

# number = int(input('Enter a number: '))

# for i in range(11):
#     print(f"{number} X {i} = {number * i}")




# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

# total = sum_nums = 0

# for i in range(10):
#     number = int(input("Enter number: "))
#     total += 1
#     sum_nums += number



# Imprimir los números múltiplos de 3 entre el 1 y el 10.

# for i in range(1, 10):
#     if i % 3 != 0:
#         continue
#     print(i)        


# Mostrar los números pares que hay desde la unidad hasta el número 50.

# for i in range(1 ,51):
#     if i % 2 == 0:
#         print(i, end=',')
#         continue
    
# for i in range(2 ,51, 2):
#     print(i, end=',')



# Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# number = int(input('Enter number: '))

# for i in range(1, number + 1):
#     for j in range(1, i+1,):
#         print(j, end='')
#     print('')



# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

# number = int(input('Enter number: '))
# dividers = 1

# for i in range(1, (number//2)+1 ):
#     if number % i == 0:
#         dividers += 1
        
# print(f'Number: {number}\tTotal of dividers: {dividers}')


# Ingresar un número. Determinar si el número es primo o no.

# number = int(input('Enter number: '))
# dividers = 1

# for i in range(1, (number//2)+1 ):
#     if number % i == 0:
#         dividers += 1
    
# print(f'Number {number} is prime') if dividers == 2 else print(f'Number {number} is not prime')



# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

# number = int(input('Enter number: '))
# prime_numbers = 0

# for i in range(1, number+1):
#     dividers = 1
#     for j in range(1, (i//2)+1 ):
#         if i % j == 0:
#             dividers += 1
#             if dividers > 2: 
#                 break
#     if dividers == 2:
#         prime_numbers += 1
#         print(i, end=' ')

# print(f'\nPrime numbers between 1 and {number}: {prime_numbers}')
        
            