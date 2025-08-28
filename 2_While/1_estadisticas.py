# cSpell: disable

# WHILE
# Contadores - Acumuladores - Máximos y mínimos
# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

num = 1
while num < 11:
    print(num)
    num += 1

# =========================================================================================
print(50*"=")
# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

num = 10
while num > 0:
    print(num)
    num -= 1

# =========================================================================================
print(50*"=")
# Mostrar la suma de los números desde el 1 hasta el 10.

acumulador = 0
num = 1

while num < 11:
    acumulador += num
    num += 1 
print(f'La suma de los numeros del 1 al 10 es: {acumulador}')

# =========================================================================================
print(50*"=")
# Mostrar la suma de los números pares desde el 1 hasta el 10.

acumulador = 0
num = 2

while num < 11:
    acumulador += num
    num += 2 
print(f'La suma de los numeros pares del 1 al 10 es: {acumulador}')

# =========================================================================================
print(50*"=")
# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.


# =========================================================================================
print(50*"=")
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
# =========================================================================================
print(50*"=")
# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
# =========================================================================================
print(50*"=")
# Ingresar 10 números enteros. Determinar el máximo y el mínimo.
