from random import randint
from paquete_input.Input import get_int

OPCIONES = {1: 'Piedra', 2: 'Papel', 3: 'Tijera'}

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """ 
    Determina quién ganó la ronda según las elecciones del jugador y la máquina
    
    Args:
        jugador (int):  Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera)
        maquina (int):  Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera)
        
    Returns:
        str:    "Jugador" → Si el jugador gana la ronda
                "Maquina" → Si la máquina gana la ronda
                "Empate" → Si ambos eligen el mismo elemento
    """
    
    if jugador == maquina:
        return "Empate"
    
    if (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    
    return "Maquina" 
    
def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int)  -> bool:
    """
    Determina si la partida sigue en curso o ya ha finalizado.
    
    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina
        ronda_actual (int): Número de la ronda actual
    
    Returns:
        bool:   True → Si la partida sigue en curso.
                False → Si la partida ha finalizado
    """
    
    if abs(aciertos_jugador - aciertos_maquina) == 2 or (ronda_actual == 3 and aciertos_jugador != aciertos_maquina):
        return False
    
    return True
    
def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """
    Determina quién ganó la partida comparando los aciertos finales
    
    Args:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina
        
    Returns:
        str:    "Jugador" → Si el jugador tiene más aciertos
                "Maquina" → Si la máquina tiene más aciertos
    """
    
    return "Jugador" if aciertos_jugador > aciertos_maquina else "Maquina"

def mostrar_elemento(eleccion: int) -> str:
    """
    Convierte la elección numérica en un texto legible
    
    Args:
        eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera)
        
    Returns:
        str:    "Piedra" cuando su elección == 1
                "Papel" cuando su elección == 2
                "Tijera" cuando su  elección == 3
    """
    return OPCIONES[eleccion]

def jugar_piedra_papel_tijera() -> str:
    """
    Gestiona toda la lógica del juego, usando las funciones anteriores
    
    Returns:
        str:    Devuelve quien ganó la partida ("Jugador"|"Maquina")
    """
    rondas_jugadas = puntos_jugador = puntos_maquina = 0
    ganador = ''
    
    while True:
        rondas_jugadas += 1
        eleccion_jugador = get_int('1.Piedra \n2.Papel \n3.Tijera\nSeleccione una opción: ', 'Debe ingresar una opción válida', 1, 3)
        eleccion_maquina = randint(1, 3)
        
        ganador_ronda = verificar_ganador_ronda(eleccion_jugador, eleccion_maquina)
        if ganador_ronda == 'Jugador':
            puntos_jugador += 1
        elif ganador_ronda == 'Maquina':
            puntos_maquina += 1
        
        print()
        print(f'RONDA {rondas_jugadas}\t\tPuntos\tJugador: {puntos_jugador}|Maquina: {puntos_maquina} ')
        print('-'*75)
        print(f'Jugador: {mostrar_elemento(eleccion_jugador):<15} Maquina: {mostrar_elemento(eleccion_maquina):<15}\t||Ganador: {ganador_ronda}')
        print('-'*75)
        print()
            
        if rondas_jugadas == 1:
            continue
        
        if not verificar_estado_partida(puntos_jugador, puntos_maquina, rondas_jugadas):
            ganador = verificar_ganador_partida(puntos_jugador, puntos_maquina)
            break;
        
    return ganador

def main():
    ganador = jugar_piedra_papel_tijera()
    print(f'El ganador de la partida fue: {ganador}')
    
if __name__ == '__main__':
    main()

