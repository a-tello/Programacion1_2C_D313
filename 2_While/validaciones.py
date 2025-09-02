# WHILE
# Validaciones

# # # # # # # # # # # # # # # # # # # # # # # 
#                                           #
#  Uncomment the lines to execute the code  #
#                                           #
# # # # # # # # # # # # # # # # # # # # # # # 


# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

# password = 'admin123'

# while True:
#     usr_password = input('Enter password: ')
#     if usr_password == password:
#         print('Correct')
#         break
    
#     print('Error.')
    
    
# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

# attempts_available = 3
# password = 'admin123'
# attempts = 0

# while attempts < attempts_available:
#     usr_password = input('Enter password: ')
#     if usr_password == password:
#         print('Correct')
#         break
#     print(f'Error. Attempts remaining: {attempts_available-1-attempts} ')
#     attempts += 1
# else:
#     print(f'User locked')
   
    

# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

# test_score = 0
    
# while True:
#     test_score = int(input('Enter test score (1-10): '))
#     if 0 < test_score < 11:
#         print(f'Your test score is {test_score}')
#         break
#     print('Error. Score must be between 1 and 10')



# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

# colors = ['rojo', 'verde', 'azul']

# while True:
#     usr_color = input('Enter a color: ').lower()
#     if usr_color in colors:
#         print('Valid color')
#         break
#     print(f'Error. {usr_color.capitalize()} is not a valid color')
        
    


# Integrador Validaciones
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
#  
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
# 
# Una vez ingresados y validados los datos, mostrarlos por pantalla.

# last_name = ''
# age = 0
# civil_state = ''
# civil_state_opt = ['soltero', 'soltera', 'casado', 'casada', 'divorciado', 'divorciada', 'viudo', 'viuda']
# id_number = 0

# while True:
#     last_name = input('Enter last_name: ').lower()
#     if last_name.isalpha():
#         break
#     print('Error. Last name must contain only letters')
    
# while True:
#     age = int(input('Enter your age: '))
#     if 17 < age < 91:
#         break
#     print('Error. Age must be between 18 and 90')
    
# while True:
#     civil_state = input('Enter civil state: ').lower()
#     if civil_state in civil_state_opt:
#         break
#     print('Error. Civil State must be: "Soltero/a, "Casado/a, Divorciado/a, Viudo/a"')
    
# while True:
#     id_number = int(input('Enter id number: '))
#     if 999 < id_number < 10000:
#         break
#     print('Error. Id number must contain 4 digits')
    

# print(f"""
#       INFO
#       {'='*50}
#       Last Name: {last_name.capitalize()}
#       Age: {age}
#       Civil State: {civil_state.capitalize()}
#       ID number: {id_number}
#       """)