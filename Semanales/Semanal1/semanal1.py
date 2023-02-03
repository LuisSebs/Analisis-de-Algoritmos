"""
    Semanal: 1
    Arrieta Mancera Luis Sebastian (318174116)
    Martinez Hernandez Zuriel Enrique (318056423)
    Semestre 2023-2

    Recursos:
    Sobrecarga de metodos: https://www.geeksforgeeks.org/python-method-overloading/
    Modificadores de acceso: http://www.tugurium.com/python/index.php?C=PYTHON.11#:~:text=El%20modificador%20de%20acceso%20establece,que%20se%20convierta%20en%20privado.
    Convenciones: https://cosasdedevs.com/posts/convencion-nombres-python/
"""

import random
import math

class Colors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Perla():
    """
        Clase que representa a una perla
    """
    peso: int

    # Al impimir unicamente una instancia se llama este metodo
    def __str__(self) -> str:
        # Imprimimos el peso de la Perla
        return str(self.peso)

    # Al imprimir un arreglo para cada instancia se llama este metodo
    def __repr__(self) -> str:
        # Mandamos a llamar el etodo __str__()
        return self.__str__()

class PerlaReal(Perla):
    """
        Clase extendida de perla que representa una perla real
    """
    # Asignamos el peso (atributo heredado de Perla)
    def __init__(self) -> None:
        self.peso = 1
        super().__init__()
    # Implementamos la representacion del objeto al imprimir (heredada de Perla)
    def __str__(self) -> str:
        return super().__str__()

class PerlaFalsa(Perla):
    """
        Clase extendida de Perla que representa una perla falsa
    """
    # Asignamos el peso (atributo heredado de Perla)
    def __init__(self) -> None:
        self.peso = 0
        super().__init__()
    # Implementamos la representacion del objeto al imprimir (heredada de Perla)
    def __str__(self) -> str:
        return super().__str__()

class Balanza():
    # Numero de veces que se usa la Balanza
    contador = 0

    """
        Clase que representa a la balanza
    """
    def __suma_peso(conjunto):
        """
            Suma el peso total de un conjunto de perlas
        """
        peso_total = 0
        for elemento in conjunto:
            peso_total = peso_total + elemento.peso
        return peso_total

    def pesa(conjunto1, conjunto2) -> int:
        """
            Pesa el conjunto1 y el conjunto2.
            Regresa 0 si ambos conjuntos pesan lo mismo, 1 si
            el conjunto 2 es mas pesado y -1 si el conjunto 1 es 
            mas pesado.

            Args:
                conjunto1: arreglo de perlas
                conjunto2: arreglo de perlas
        """
        Balanza.contador = Balanza.contador+1
        # self es como el this de java y tiene que ser pasado como parametro
        pesoIzquierdo = Balanza.__suma_peso(conjunto1)
        pesoDerecho = Balanza.__suma_peso(conjunto2)
        
        if pesoDerecho == pesoIzquierdo:
            return 0 
        elif pesoDerecho > pesoIzquierdo:
            return 1 
        else:
            return -1

    def pesaUnitario(perla1,perla2) -> int:
        """
            Pesa la perla1 y la perla2
            Regresa 0 si ambas perlas pesan lo mismo, 1 si
            la perla2 es mas pesada y -1 si la perla1 es 
            mas pesada.

            Args:
                perla1: Perla
                perla2: Perla
        """
        pesoI = perla1.peso
        pesoD = perla2.peso

        if pesoI == pesoD:
            return 0 # Pesan lo mismo
        elif pesoD > pesoI:
            return 1 # El lado derecho pesa mas
        else: # El lado izquierdo pesa mas
            return -1

def conjuntoDePerlas(cantidad):
    """
        Regresa un arreglo con la cantidad de
        perlas ingresada como parámetro, una 
        de ellas es falsa y la coloca
        en un lugar random

        Args:
            cantidad: cantidad de perlas del arreglo a regresar

        Nota: la cantidad tiene que ser positiva: cantidad > 0
    """
    # Arreglo a regresar
    arreglo = list()

    # Iterador
    i = 0
    
    # Posicion de la perla falsa
    posicion_perla_falsa = random.randint(0,cantidad-1)

    # Creamos y agregamos las perlas al arreglo
    while cantidad > i :
        if i == posicion_perla_falsa:
            arreglo.append(PerlaFalsa())
        else:
            arreglo.append(PerlaReal()) 
        i = i + 1

    return arreglo

def encuentraPerlaFalsaTiempoLineal(arreglo) -> int:

    """
        Regresa la posicion de la perla falsa 
        de un arreglo con perlas reales
        y una falsa en tiempo O(log n)
    """

    # Longitud del arreglo
    n = len(arreglo)

    # Pesamos una por una
    for i in range(n):
        estatus = Balanza.pesaUnitario(arreglo[i],arreglo[i+1])
        if estatus == 1:
            return i
        elif estatus == -1:
            return i+1
        else:    
            continue
    
    # En caso de que no exista una perla falsa dentro del conjunto
    return None

def encuentraPerlaFalsaUsando2VecesLaBalanza(arreglo) -> int:
    """
        Encuentra la perla falsa
        para un conjunto de 8 perlas
        usando unicamente dos veces la balanza
    """
    posicion = 0
    conjunto = arreglo

    # Dividimos el conjunto en 3
    conjunto1 = conjunto[0:3]
    conjunto2 = conjunto[3:6]
    conjunto3 = conjunto[6:8]

    # Primer uso de la balanza
    estatus = Balanza.pesa(conjunto1,conjunto2)

    # Vemos que conjunto contiene la perla falsa
    if estatus == 0:
        # La perla esta en el conjunto 3
        conjunto = conjunto3
        # Por lo tanto las primeras 6 perlas son reales
        posicion = 6
    elif estatus == 1:
        # La perla esta en el conjunto 1
        conjunto = conjunto1
        """
        Puede que se encuentre en las primeras posiciones
        por eso no modificamos la posicion
        """
    else:
        # La perla se encuentra en el conjunto 2
        conjunto = conjunto2
        # Las primeras 3 perlas son reales
        posicion = 3

    # Veamos si el conjunto se puede dividir en 3 o en 2
    if  len(conjunto)%3 == 0:
        conjunto1 = conjunto[0:1]
        conjunto2 = conjunto[1:2]
        conjunto3 = conjunto[2:3]
    else:
        conjunto1 = conjunto[0:1]
        conjunto2 = conjunto[1:2]

    # Segundo uso de la balanza
    estatus = Balanza.pesa(conjunto1,conjunto2)

    if estatus == 0:
        # La perla esta en el conjunto 3
        posicion = posicion + 2
    elif estatus == 1:
        # La perla esta en el conjunto 1
        pass
    else:
        # La perla esta en el conjunto 2
        posicion = posicion + 1
    return posicion

def encuentraPerlaFalsaTiempoLogN(arreglo) -> int:
    """
        Regresa la posicion de la perla falsa 
        de un arreglo con perlas reales
        y una falsa en tiempo O(log n)

        Args:
            arreglo: arreglo de perlas

        Nota: el arreglo debe contener
        solo una perla falsa
    """
    # Longitud del arreglo
    lent = len(arreglo)
    return encuentraPerlaFalsaTiempoLogNAux(arreglo=arreglo,posicion=0,longitud=lent)

def encuentraPerlaFalsaTiempoLogNAux(arreglo,posicion,longitud) -> int:
    """
        Regresa la posicion de la perla falsa 
        de un arreglo con perlas reales
        y una falsa dada una posicion

        Args:
            arreglo: arreglo de perlas
    """
    # Determinamos si la cantidad de perlas es par o impar
    if (longitud % 2) == 0: 
        return par(arreglo,posicion=posicion,longitud=longitud)
    else:
        return impar(arreglo,posicion=posicion,longitud=longitud)
    
def par(arreglo,posicion,longitud) -> int:

    """
        Regresa la posicion de la perla falsa
        dado un arreglo de longitud par y una posicion

        Args:
            arreglo: arreglo de perlas de longitud par
            posicion: posiciones recorridas
    """
    # Longitud del arreglo
    n = longitud
    mitad = int(n/2)

    # Dividimos el conjunto a la mitad
    conjunto1 = arreglo[0:mitad]
    conjunto2 = arreglo[mitad:n]

    # Pesamos ambos conjuntos
    estatus = Balanza.pesa(conjunto1=conjunto1,conjunto2=conjunto2)

    # Verificamos el estatus
    if estatus == 0:
        return -1 # No hay ninguna posicion del arreglo con perla falsa
    elif estatus == 1: # La perla false se encuentra en el lado izquierdo
        if len(conjunto1)==1:
            return posicion
        else:
            return encuentraPerlaFalsaTiempoLogNAux(conjunto1,posicion=posicion,longitud=mitad)
    else: # La perla se encuentra en el lado derecho
        if len(conjunto2)==1:
            return posicion + 1
        else:
            return encuentraPerlaFalsaTiempoLogNAux(conjunto2,posicion=posicion + mitad,longitud=mitad)

def impar(arreglo,posicion,longitud) -> int:
    """
        Regresa la posicion de la perla falsa
        dado un arreglo de longitud impar y una posicion

        Args:
            arreglo: arreglo de perlas de longitud impar
            posicion: posiciones recorridas
    """
    # Longitud del arreglo
    n = longitud
    mitad = int((n-1)/2)

    # Dividimos el conjunto a la mitad
    conjunto1 = arreglo[0:mitad+1]
    conjunto2 = arreglo[mitad+1:n]

    # Pesamos ambos conjuntos
    estatus = Balanza.pesa(conjunto1=conjunto1,conjunto2=conjunto2)

    # Verificamos el estatus
    if estatus == 0: # La perla falsa esta del lado izquierdo
        return encuentraPerlaFalsaTiempoLogNAux(conjunto1,posicion=posicion,longitud=mitad+1)
    elif estatus == -1: # La perla falsa esta del lado derecho
        if len(conjunto2) == 1:
            return posicion + mitad + 1
        else:
            return encuentraPerlaFalsaTiempoLogNAux(conjunto2,posicion=posicion+mitad+1,longitud=mitad)
    else:
        """
            En este caso nunca se entra por como realizamos la division del arreglo,
            el lado derecho nunca puede pesar más que el lado izquierdo.
        """
        return None 


print(Colors.HEADER +
"""
Hay 8 perlas, todas exactamente iguales en apariencia y tacto. Cada una pesa exactamente lo mismo
salvo una, que es falsa y pesa ligeramente menos.

""" + Colors.ENDC)
# Conjunto de perlas
perlas = conjuntoDePerlas(8)
print(f"Perlas: {perlas}")

# Brinda un algoritmo que encuentre la perla falsa en tiempo Θ(n)
posicion1 = encuentraPerlaFalsaTiempoLineal(perlas)
print(Colors.HEADER +
"""

Brinda un algoritmo que encuentre la perla falsa en tiempo Θ(n)

""" + Colors.ENDC)
print(f"La posicion de la perla falsa es: {posicion1}")

# Brinda un algoritmo que encuentre la perla falsa usando la balanza maximo 2 veces.
posicion2 = encuentraPerlaFalsaUsando2VecesLaBalanza(perlas)
print(Colors.HEADER +
"""

Brinda un algoritmo que encuentre la perla falsa usando la balanza maximo 2 veces.

""" + Colors.ENDC)
print(f"La posicion de la perla falsa es: {posicion2}")

"""
Generalizando el problema para recibir un grupo de n perlas en las que una es falsa. Brinda un
algoritmo que encuentre la perla falsa en tiempo O(log n)
"""
posicion3 = encuentraPerlaFalsaTiempoLogN(perlas)
print(Colors.HEADER +
""" 

Generalizando el problema para recibir un grupo de n perlas en las que una es falsa. 
Brinda un algoritmo que encuentre la perla falsa en tiempo O(log n)

""" + Colors.ENDC)

print(f"La posicion de la perla falsa es: {posicion3}")


print(Colors.HEADER +
"""

Si el problema fuera sobre 1234 perlas en lugar de 8, ¿Cuantas veces es suficiente usar la balanza para
encontrar la perla falsa utilizando la estrategia del inciso anterior? 

""" + Colors.ENDC)

perlas = conjuntoDePerlas(1234)
Balanza.contador = 0
posicion4 = encuentraPerlaFalsaTiempoLogN(perlas)
numero_de_usos = Balanza.contador
print(f"La posicion de la perla falsa es: {posicion4}")
print(f"El numero de usos de la balanza fue: {numero_de_usos}")
print(Colors.WARNING + 
"""
NOTA: El numero de usos de la balanza depende de la posicion de la perla,
ya que a veces se divide en dos conjuntos del mismo tamaño y a veces en
dos conjuntos de tamaño diferente. Esto ocurre por la division de numeros
pares e impares, dependiendo de la posicion de la perla falsa
se puede tomar un conjunto par o impar.
""")




