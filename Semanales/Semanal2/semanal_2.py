import math

class Colors():
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GRAY = '\033[0m'
    WHITE = '\033[0;0m'
    UNDERLINE = '\033[4m'

    def sample():
        """
            Imprime una muestra de todos los colores
            disponibles en esta clase.
        """

        print(Colors.PURPLE + "hola")
        print(Colors.BLUE + "hola")
        print(Colors.CYAN + "hola")
        print(Colors.GREEN + "hola")
        print(Colors.YELLOW + "hola")
        print(Colors.RED + "hola")
        print(Colors.GRAY + "hola")
        print(Colors.WHITE + "hola")
        print(Colors.UNDERLINE + "hola")

class Jugador():

    """
        Clase jugador

        Attributes:
            numero (int): numero del jugador
    """
    
    numero: int

    def __init__(self, numero:int) -> None:
        self.numero = numero

    def __repr__(self) -> str:
        return str(self.numero)

def jugadores(cantidad:int) -> list:    
    
    """
        Regresa un conjunto de jugadores enumerados del 1 hasta la cantidad ingresada

        Args:
            cantidad: cantidad de jugadores
    """

    # Creamos el conjunto
    jugadores = list()

    # Agregamos a los jugadores
    for i in range(cantidad):
        jugador = Jugador(i+1)
        jugadores.append(jugador)

    return jugadores

def ganadorTethaN(jugadores:list,inicio:int) -> Jugador:
    """
        Regresa el ganador del juego. Encuentra el jugador ganador en tiempo Θ(n)

        Args:
            jugadores: un conjunto de jugadores
            inicio: posicion de la persona que tiene el arma
    """

    # Creamos una copio de los jugadores para no modificar el original
    jugadores = jugadores.copy()

    # Cantidad de jugadores
    n = len(jugadores)
    # Posicion del jugador que tiene el arma
    p = inicio - 1
    # Numero de personas vivas
    v = n

    # Realizamos n-1 asesinatos
    for i in range(n-1):

        # Caso en el que el jugador a eliminar sea el que inicio la ronda
        if p + 1 == v:
            p = -1
        
        # Eliminamos al jugador de la izquierda
        del jugadores[p+1]
        # Reducimos el numero de personas vivas
        v = v - 1 
        # Le damos el arma a la persona viva más próxima a la izquierda
        p = p + 1

        # Caso en el que la persona a la que le tengamos que pasar el arma sea la que inicio la ronda
        if p == v:
            p = v%p

    # Regresamos a la persona ganadora
    return jugadores[0]

def ganadorOPequeniaN(jugadores:list,inicio:int) -> Jugador:

    """
        Encuentra el jugador ganador en tiempo o(n)

        Args:
            jugadores: un conjunto de jugadores
            inicio: posicion de la persona que tiene el arma
    """
    # Numero de jugadores
    n = len(jugadores)
    
    # Exponente calculado de Log_2 n 
    exp = math.floor(math.log(n,2))
    
    # La menor potencia de 2 mas cercana a n
    power_of_two = 2**exp
    
    # Numero de personas que tienen que morir antes de que el numero de personas vivas se combierta en potencia de 2
    deaths = n-power_of_two

    # Posiciones recorrias considerando el lugar del jugador inicial
    ganador = ((deaths * 2) + inicio)%n
    
    return jugadores[ganador-1]

def sobrevivir(cantidad:int,tu_posicion:int) -> int:
    """
        Regresa la posicion del jugador al que le tienen que dar el arma
        para que puedas sobrevivir.

        Args:
            jugadores: cantidad de jugadores
            tu_posicion: tu posicion en el juego
    """
    # Numero de jugadores
    n = cantidad
    
    # Exponente calculado de Log_2 n 
    exp = math.floor(math.log(n,2))
    
    # La menor potencia de 2 mas cercana a n
    power_of_two = 2**exp
    
    # Numero de personas que tienen que morir antes de que el numero de personas vivas se combierta en potencia de 2
    deaths = n-power_of_two

    # Numero de lugares a desplazar
    places = deaths * 2

    # Posicion de la persona a la que le tenemos que dar el arma para sobrevivir
    pos = tu_posicion - places

    # En caso de que el desplazamiento sea negativo
    if pos < 0:
        pos = n + pos

    return pos

def semanal():
    """
        Muestra una simulacion del semanal
    """
    texto_ejercicio1 = "Si al iniciar el juego, le dan un arma a la persona etiquetada con el numero 1"
    texto_1incisoI = "i. Menciona quien sera el sobreviviente. Justifica tu respuesta."
    texto_1incisoII = "ii. Si el juego consistiera en n personas, brinda un algoritmo que indique quien sera el sobreviviente en tiempo Θ(n)."
    texto_ejercicio2 = "2. Si al iniciar el juego, le dan un arma a la persona etiquetada con el numero r (y solo a esa persona):"
    texto_2incisoI =  "i. Si el juego consistiera en n personas, brinda un algoritmo que indique quien sera el sobreviviente en tiempo o(n)."
    texto_2incisoII = """ii. Si el juego consistiera en n personas, tu eres parte del juego, a ti te toco ser el numero p en el circulo y, por diversion, 
        los guardias te dan la oportunidad de decir a que jugador deben entregarle el arma para comenzar el juego, 
        ¿que numero r deberias decirles si quieres sobrevivir?"""
    
    """
        EJERCICIO 1 INCISO i
    """
    print("\n"+Colors.PURPLE + texto_ejercicio1)
    print(Colors.GREEN+ "\n\t" + texto_1incisoI)
    # Conjunto de jugadores
    c1 = jugadores(100)
    # Ganador
    ganador_incisoi = ganadorTethaN(jugadores=c1,inicio=1)
    print(Colors.WHITE + f"\n\t\tPara {Colors.RED} n = 100 {Colors.WHITE} y el jugador inicial {Colors.CYAN} 1 {Colors.WHITE} el ganador es el jugador {Colors.YELLOW} {ganador_incisoi}")
    
    """
        EJERCICIO 1 INCISO ii
    """
    print(Colors.GREEN+ "\n\t" + texto_1incisoII)
     # Cantiad de jgadores
    n = 200
    # Conjunto de jugadores
    c = jugadores(n)
    # Posicion inicial
    i = 50
    # Ganador tiempo Tetha(n)
    ganador_tiempo_tethaN = ganadorTethaN(jugadores=c,inicio=i)
    print(Colors.WHITE + f"\n\t\tPara {Colors.RED} n = {n} {Colors.WHITE} y el jugador inicial {Colors.CYAN} {i} {Colors.WHITE} el ganador en tiempo Θ(n) es el jugador {Colors.YELLOW} {ganador_tiempo_tethaN}")

    """
        EJERCICIO 2 INCISO i
    """
    print("\n\n"+Colors.PURPLE + texto_ejercicio2)    
    print(Colors.GREEN+ "\n\t" + texto_2incisoI)
    # Cantiad de jgadores
    n = 200
    # Conjunto de jugadores
    c = jugadores(n)
    # Posicion inicial
    i = 50
    ganador_tiempo_o_n = ganadorOPequeniaN(jugadores=c,inicio=i)
    print(Colors.WHITE + f"\n\t\tPara {Colors.RED} n = {n} {Colors.WHITE} y el jugador inicial {Colors.CYAN} {i} {Colors.WHITE} el ganador en tiempo o(n) es el jugador {Colors.YELLOW} {ganador_tiempo_o_n}")
    print(Colors.GREEN+ "\n\t" + texto_2incisoII)

    """
        EJERCICIO 2 INCISO ii
    """
    # Numero de jugadores
    n = 100
    # Tu posicion
    tu_posicion = 1
    # Posicion inicial para sobrevivir
    jugador_inicial =sobrevivir(cantidad=n,tu_posicion=tu_posicion)
    print(Colors.WHITE + f"\n\t\tPara n = {Colors.RED} {n} {Colors.WHITE} y tu posicion {Colors.CYAN} {tu_posicion} {Colors.WHITE} si quieres sobrevivir el jugador inicial debe de ser el jugador {Colors.YELLOW} {jugador_inicial} {Colors.WHITE} \n")

# Corremos la simulacion del semanal
semanal()














