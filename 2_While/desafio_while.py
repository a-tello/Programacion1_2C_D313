# 📌 Desafío: Encuesta Tecnológica en UTN Technologies
# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado.
# Las tecnologías en evaluación son:
#  🔹 Inteligencia Artificial (IA)
#  🔹 Realidad Virtual/Aumentada (RV/RA)
#  🔹 Internet de las Cosas (IOT)
# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas.
# 🔹 Recolección de Datos
# Cada empleado encuestado deberá proporcionar la siguiente información:
#  ✔️ Nombre
#  ✔️ Edad (debe ser 18 años o más)
#  ✔️ Género (Masculino, Femenino, Otro)
#  ✔️ Tecnología elegida (IA, RV/RA, IOT)
# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal.
# 🔹 Análisis de Datos
# A partir de las respuestas, se deben calcular las siguientes métricas:
# 1️⃣ Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive).
# 2️⃣ Porcentaje de empleados que NO votaron por IA, siempre y cuando:
# Su género no sea Femenino 
# Su edad está entre los 33 y 40 años.
# 3️⃣ Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.


# 🔹 Requisitos del Programa
#  ✔️ Los datos deben solicitarse y validarse correctamente.
#  ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis.
#  ✔️ Presentar los resultados de manera clara y organizada.


EMPLOYEES = 10
answers = age = 0
name = gender = technology = ''
genders = ['male', 'female', 'other']
technologies = ['IA', 'RV/RA', 'RV', 'RA', 'IOT']
male_employees_IOT_IA_btw_25_50 = 0
not_female_employees_notIA_btw_33_40 = 0
oldest_male_employee_age = 0
oldest_male_employee_name = ''
oldest_male_employee_technology = ''


while answers < EMPLOYEES:
    
    while True:
        name = input('Enter name: ').lower()
        if name.isalpha():
            break
        print('Error. Name must be contain only letters')
        
    while True:
        age = int(input('Enter age: '))
        if 17 < age < 90:
            break
        print('Error. Age must be between 18 and 90')
                
    while True:
        gender = input('Enter gender (Male, Female, Other): ').lower()
        if gender in genders:
            break
        print('Error. Gender must be: "Male", "Female", "Other"')
        
    while True:
        technology = input('Enter technology (IA, RV/RA, IOT): ').upper()
        if technology in technologies:
            break
        print('Error. Technolgy must be: "IA", "RV/RA", "IOT"')
        
    # Number of male employees who voted for IA or IOT (Between 25 and 50)
    if gender == 'male' and 25 < age < 50 and technology in ['IA', 'IOT']:
        male_employees_IOT_IA_btw_25_50 += 1
    
    
    # Calculate % employees who didn't vote IA (No female. Between 33 and 40y.o)
    if gender != 'female' and 32 < age < 41 and technology != 'IA':
        not_female_employees_notIA_btw_33_40 += 1
    
    
    # Oldest male employee info
    if gender == 'male' and age > oldest_male_employee_age:
        oldest_male_employee_age = age
        oldest_male_employee_name = name
        oldest_male_employee_technology = technology

    
    answers += 1
    
print(f"""
      Results
      {50*'='}
      Number of male employees who vote for IA or IOT (between 25 and 50): {male_employees_IOT_IA_btw_25_50}
      Percentage of employees who dind't vote for IA (Not female, between 33 and 40): %{(not_female_employees_notIA_btw_33_40 / EMPLOYEES) * 100}
      Older male employee: {oldest_male_employee_name.capitalize()} vote for {oldest_male_employee_technology}
        """)