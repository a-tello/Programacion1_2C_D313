from .Validate import *

def get_int(msg: str, err_msg: str, min_int: int, max_int: int, retries: int = -1) -> int|None:
    """
    Pide un número entero. Valida que la entrada sea correcta y se encuentre en el rango especificado.
    
    Args:
        msg (str): mensaje para pedir el número
        err_msg (str): mensaje de error en caso de que la entrada no sea válida
        min_int (int): número mas bajo del rango de validez
        max_int (int): número mas alto del rango de validez
        retries (int): cantidad de intentos para ingresar un número. Si no se pasa valor, tendrá intentos ilimitados.
        
    Returns:
        int:    número entero ingresado y validado
        None:   si no ingresa un número válido y se queda sin intentos
    """
    while True:
        num = input(msg)
        retries -= 1
        
        if validate_number(num, min_int, max_int):
            num = int(num)
            return num 
        
        if retries == 0: break
        
        print(err_msg)    
    return None



def get_float(msg: str, err_msg: str, min_int: float, max_int: float, retries: int = -1) -> float|None:
    """
    Pide un número flotante. Valida que la entrada sea correcta y se encuentre en el rango especificado.
    
    Args:
        msg (str): mensaje para pedir el número
        err_msg (str): mensaje de error en caso de que la entrada no sea válida
        min_int (float): número mas bajo del rango de validez
        max_int (float): número mas alto del rango de validez
        retries (int): cantidad de intentos para ingresar un número. Si no se pasa valor, tendrá intentos ilimitados.
        
    Returns:
        float:  número flotante ingresado y validado
        None:   si no ingresa un número válido y se queda sin intentos
    """
    while True:
        num = input(msg)
        retries -= 1
        
        if validate_number(num, min_int, max_int):
            num = float(num)
            return num 

        if retries == 0: break
        
        print(err_msg)      
    return None


def get_string(msg: str, err_msg: str, length: int, retries: int = -1) -> str|None:
    """
    Pide una cadena de caracteres. Valida que la entrada cumpla con un largo mínimo.
    
    Args:
        msg (str): mensaje para pedir la cadena
        err_msg (str): mensaje de error en caso de que la entrada no sea válida
        length (int): longitud mínima que debe tener la cadena ingresada
        retries (int): cantidad de intentos para ingresar una cadena. Si no se pasa valor, tendrá intentos ilimitados.
        
    Returns:
        str:    cadena ingresada y validada
        None:   si no ingresa una cadena válida y se queda sin intentos
    """
    while retries > 0:
        string = input(msg)
        retries -= 1
            
        if validate_length(string, length):
            return string
        
        print(err_msg)    
    return None



# print(get_int('Ingrese un número entero entre 1 y 10: ', 'Número inválido', 1, 10))
# print(get_float('Ingrese un número entero entre 1 y 10: ', 'Número inválido', 1, 10, 3))
# print(get_string('Ingrese una cadena de mínimo 6 caracteres: ', 'Cadena inválida. Debe contener al menos 6 caracteres', 6, 3))

