# cSpell: disable

# # # # # # # # # # # # # # # # # # # # # # # 
#                                           #
#  Uncomment the lines to execute the code  #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # # 




# WHILE
# Contadores - Acumuladores - Máximos y mínimos
# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# num = 1
# while num < 11:
#     print(num)
#     num += 1

# =========================================================================================
# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# num = 10
# while num > 0:
#     print(num)
#     num -= 1

# =========================================================================================
# Mostrar la suma de los números desde el 1 hasta el 10.

# acc = 0
# num = 1

# while num < 11:
#     acc += num
#     num += 1 
# print(f'Sum of numbers (1-10): {acc}')

# =========================================================================================
# Mostrar la suma de los números pares desde el 1 hasta el 10.

# acc = 0
# num = 2

# while num < 11:
#     acc += num
#     num += 2 
# print(f'Sum of even numbers(1-10): {acc}')

# =========================================================================================
# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

# NUMBERS = 5
# sum = 0
# avg = 0
# i = 0

# while i < NUMBERS:
#     num = int(input('Enter a number: '))
#     sum += num
#     i += 1

# avg = sum / NUMBERS
# print(f"""
#         Sum: {sum}
#         Average: {avg}
# """)


# =========================================================================================
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# sum = 0
# avg = 0
# numbers = 0

# while True:
#     num = int(input('Enter a number: '))
#     sum += num
#     numbers += 1
#     op = input('Do you want to enter another number? (Y/N): ').upper()
#     if op != 'Y':
#         break

# avg = sum / numbers
# print(f"""
#         Sum: {sum}
#         Average: {avg}
# """)

# =========================================================================================
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

# sum = 0
# product = 1

# while True:
#     num = int(input('Enter a number: '))
#     if num > 0:
#         sum += num
#     else:
#         product *= num

#     op = input('Do you want to enter another number? (Y/N): ').upper()
#     if op != 'Y':
#         break

# print(f"""
#         Sum of positive numbers: {sum}
#         Product of negative numbers: {product}
# """)

# =========================================================================================
# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# NUMBERS = 10
# i = 1
# max = min = int(input('Enter a number: '))

# while i < NUMBERS:
#     num = int(input('Enter a number: '))

#     if num > max:
#         max = num
#     if num < min:
#         min = num
    
#     i += 1

# print(f"""
#         Max: {max}
#         Min: {min}
# """)


# =========================================================================================
# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

# sum = 0
# avg = 0
# i = 0

# while True:
#     num = int(input('Enter a number: '))
#     sum += num
#     i += 1

#     if i < 5:
#         continue

#     op = input('Do you want to enter another number? (Y/N): ').upper()
#     if op != 'Y':
#         break

# avg = sum / i

# print(f"""
#         Sum : {sum}
#         Average: {avg}
# """)


# =========================================================================================
#Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

# sum = 0
# avg = 0
# i = 0

# while True:
#     num = int(input('Enter a number: '))
#     sum += num
#     i += 1

#     if i < 5:
#         continue
#     elif i > 9:
#         break

#     op = input('Do you want to enter another number? (Y/N): ').upper()
#     if op != 'Y':
#         break

# avg = sum / i

# print(f"""
#         Sum : {sum}
#         Average: {avg}
# """)




# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.


# pos_sum = neg_sum = neg_nums = pos_avg = pos_max = neg_percentage = total_nums = pos_nums = 0

# while True:
#     num = int(input('Enter a number: '))
    
#     if num > 0:
#         pos_sum += num
#         pos_nums += 1

#         if num > pos_max:
#             pos_max = num

#     elif num < 0:
#         neg_sum += num
#         neg_nums += 1

#     total_nums += 1

#     op = input('Do you want to enter another number? (Y/N): ').upper()
#     if op != 'Y':
#         break

# pos_avg = pos_sum / pos_nums
# neg_percentage = neg_nums / total_nums

# print(f"""
#         Sum of negative numbers: {neg_sum} 
#         Sum of positive numbers: {pos_sum} 
#         Total of negative numbers: {neg_nums} 
#         Average of positive numbers: {pos_avg} 
#         Max of positive numbers: {pos_max} 
#         Percentage of negative numbers negative/total: %{neg_percentage*100} 
# """)
