"""
    Semanal: 1
    Arrieta Mancera Luis Sebastian
    Semestre 2023-2

    Recursos:
    Sobrecarga de metodos: https://www.geeksforgeeks.org/python-method-overloading/
"""

import random

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
    # Implementamos la representacion del objeto a imprimir (heredada del Perla)
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
    # Implementamos la representacion del objeto a imprimir (heredada del Perla)
    def __str__(self) -> str:
        return super().__str__()

class Balanza():
    # Numero de veces que se usa la Balanza
    contador = 0

    """
        Clase que representa a la balanza
    """
    def sumaPeso(conjunto):
        """
            Suma el peso total de un conjunto de perlas
        """
        pesoTotal = 0
        for elemento in conjunto:
            pesoTotal = pesoTotal + elemento.peso
        return pesoTotal

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
        pesoIzquierdo = Balanza.sumaPeso(conjunto1)
        pesoDerecho = Balanza.sumaPeso(conjunto2)
        
        if pesoDerecho == pesoIzquierdo:
            return 0 
        elif pesoDerecho > pesoIzquierdo:
            return 1 
        else:
            return -1

    def pesaUnitario(perla1,perla2) -> int:

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
    posicionPerlaFalsa = random.randint(0,cantidad-1)

    # Creamos y agregamos las perlas al arreglo
    while cantidad > i :
        if i == posicionPerlaFalsa:
            arreglo.append(PerlaFalsa())
        else:
            arreglo.append(PerlaReal()) 
        i = i + 1

    return arreglo

def encuentraPerlaFalsaLogN(arreglo) -> int:
    """
        Regresa la posicion de la perla falsa 
        de un arreglo con perlas reales
        y una falsa

        Args:
            arreglo: arreglo de perlas

        Nota: el arreglo debe contener
        solo una perla falsa
    """
    # Longitud del arreglo
    lent = len(arreglo)
    return encuentraPerlaFalsa(arreglo=arreglo,posicion=0,longitud=lent)

def encuentraPerlaFalsa(arreglo,posicion,longitud) -> int:
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
            posicion: posiciones recorridad
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
            return encuentraPerlaFalsa(conjunto1,posicion=posicion,longitud=mitad)
    else: # La perla se encuentra en el lado derecho
        if len(conjunto2)==1:
            return posicion + 1
        else:
            return encuentraPerlaFalsa(conjunto2,posicion=posicion + mitad,longitud=mitad)

def impar(arreglo,posicion,longitud):
    """
        Regresa la posicion de la perla falsa
        dado un arreglo de longitud impar y una posicion

        Args:
            arreglo: arreglo de perlas de longitud par
            posicion: posiciones recorridad
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
        return encuentraPerlaFalsa(conjunto1,posicion=posicion,longitud=mitad+1)
    elif estatus == -1: # La perla falsa esta del lado derecho
        if len(conjunto2) == 1:
            return posicion + mitad + 1
        else:
            return encuentraPerlaFalsa(conjunto2,posicion=posicion+mitad+1,longitud=mitad)
    else:
        """
            En este caso nunca se entra por como realizamos la division del arreglo,
            el lado derecho nunca puede pesar más que el lado izquierdo.
        """
        return None 

def encuentraPerlaFalsaN(arreglo) -> int:

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
        Este metodo solo aplica para 
        un conjunto de 8 perlas 
        donde una de ellas es falsa y 
        las demas reales
    """
    posicion = 0
    n = len(arreglo)
    mitad = int(n/2)
    arr = arreglo
    

    while True:
        if n == 2:
            break
        conjunto1 = arr[0:mitad]
        conjunto2 = arr[mitad:n]
        estatus = Balanza.pesa(conjunto1=conjunto1,conjunto2=conjunto2)
        if estatus == 1: # La perla falsa se encuentra del lado izquierdo
            arr = conjunto1
        elif estatus == -1: # La perla falsa se encuentra del lado derecho
            arr = conjunto2
            posicion = posicion + mitad

        n = mitad
        mitad = int(n/2)


    if arr[0].peso > arr[1].peso:
        return posicion + 1
    elif arr[0].peso < arr[1].peso:
        return posicion
    else: 
        return -1 

# Conjunto de perlas
perlas = conjuntoDePerlas(1234)
# print(perlas)
# posicion = encuentraPerlaFalsaUsando2VecesLaBalanza(perlas)
posicionPerlaFalsa = encuentraPerlaFalsaLogN(perlas)
print(f"La posicion de la perla falsa es: {posicionPerlaFalsa}")
print(f"Comprobacion: {perlas[posicionPerlaFalsa]}")
print(Balanza.contador)
