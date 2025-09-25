def validate_number(num_str: str, min_num: int|float, max_num: int|float) -> bool:
    try:
        valid_number = int(num_str)
        
        if min_num <= valid_number <= max_num:
            return True
    except:
        pass
    return False

def es_par(numero: int) -> bool:
    return numero % 2 == 0

def es_positivo(numero: int) -> bool:
    return True if numero > 0 else False 
    
    
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



 