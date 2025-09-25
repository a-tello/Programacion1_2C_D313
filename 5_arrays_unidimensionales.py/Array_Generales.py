import Especificas

def crear_array(cantidad: int = 0) -> list|None:
    lista = []
    if cantidad < 0: 
        print('Cantidad de elementos no válida')
        return None
    
    for i in range(cantidad):
        num = Especificas.get_int(f'Ingrese numero (pos {i + 1}): ', 'ERROR. El número debe estar entre -1000 y 1000', -1000, 1000)
        lista.append(num)
    
    return lista

def positivos_negativos_array(numeros: list) -> tuple:
    positivos = 0
    negativos = 0
    
    for numero in numeros:
        if numero == 0: continue
        
        if Especificas.es_positivo(numero):
            positivos += 1
        else:
            negativos += 1
        
    return positivos, negativos

def suma_pares(numeros: list) -> int:
    resultado = 0
    
    for numero in numeros:
        if Especificas.es_par(numero):
            resultado += numero
    
    return resultado

def mayor_numero_impar(numeros: list) -> int:
    mayor_impar = None
        
    for numero in numeros:
        if not Especificas.es_par(numero):
            if not mayor_impar or numero > mayor_impar:
                mayor_impar = numero
    
    return mayor_impar
                    

def mostrar_array(numeros: list) -> None:
    for i, numero in enumerate(numeros):
        print(f'Número: {numero}\tPos: {i + 1:<50}')
        

def mostrar_pares_array(numeros: list) -> None:
    for i, numero in enumerate(numeros):
        if Especificas.es_par(numero):
            print(f'Número: {numero}\tPos: {i + 1:<50}')
            
def mostrar_posiciones_impares_array(numeros: list) -> None:
    for i in range(0,10,2):
        print(f'Número: {numeros[i]}\tPos: {i + 1:<50}')
        
