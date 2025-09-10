import Validate

def get_int(msg: str, err_msg: str, min_int: int, max_int: int, retries: int) -> int|None:
    while retries > 0:
        num = input(msg)
        retries -= 1
        
        if Validate.validate_number(num, min_int, max_int):
            return num 

        print(err_msg)    
    return None



def get_float(msg: str, err_msg: str, min_int: float, max_int: float, retries: int) -> float|None:
    while retries > 0:
        num = input(msg)
        retries -= 1
        
        if Validate.validate_number(num, min_int, max_int):
            return num 

        print(err_msg)      
    return None


def get_string(msg: str, err_msg: str, length: int, retries: int) -> str|None:
    while retries > 0:
        string = input(msg)
        retries -= 1
            
        if Validate.validate_length(string, length):
            return string
        
        print(err_msg)    
    return None



# print(get_int('Ingrese un número entero entre 1 y 10: ', 'Número inválido', 1, 10, 3))
# print(get_float('Ingrese un número entero entre 1 y 10: ', 'Número inválido', 1, 10, 3))
# print(get_string('Ingrese una cadena de mínimo 6 caracteres: ', 'Cadena inválida. Debe contener al menos 6 caracteres', 6, 3))

