
# ANALISIS DE ALGORITMOS
# Semanal 3
# Arrieta Mancera Luis Sebastian (318174116)
# Martinez Hernandez Zuriel ENrique (318056423)

############# INCISO 1.1 ######################

# Metodo que encuentra el numero faltante en un arreglo 
# cuyos valores estan entre entre 0 y n−1.
def numeroFaltante(arreglo):
    n = len(arreglo)
    total = ((n-1) + 1)*(((n-1) + 2)/2)
    suma = sum(arreglo)
    return total - suma


# Metodo que encuentra el numero repetido en un arreglo
# cuyos valores estan entre entre 0 y n−1.
def numeroRepetido(arreglo):
    visitado = set()
    duplicado = [x for x in arreglo if x in visitado or (visitado.add(x) or False)]
    repetido = duplicado[0]
    return repetido
    
# Metodo que encuentra el numero repetido y el numero faltante 
# en un arreglo cuyos valores estan entre entre 0 y n−1
# con complejidad O(n) y espacio extra O(n).
def encuentraRyP(arreglo):
    r = numeroRepetido(arreglo)
    arreglo.remove(r)
    p = numeroFaltante(arreglo)
    print(f"\nEl numero repetido es: {r} \nEl numero que falta es: {p} \n")


############# INCISO 1.2 #########################

# Metodo que encuentra el numero repetido y el numero faltante 
# en un arreglo cuyos valores estan entre 0 y n-1
# con complejidad O(n) y espacio extra O(1).
def encuentraRyP2(arreglo):
    n = len(arreglo)
    r = 0
    p = 0
    
    for i in range(0, n):
        while arreglo[i] != arreglo[arreglo[i]]:
            tmp = arreglo[i]
            arreglo[i] = arreglo[tmp]
            arreglo[tmp] = tmp

    for i in range(0, n):
        if arreglo[i] != i and r == 0:
            p = i
            r = arreglo[i]
         
    print(f"\nEl numero repetido es: {r} \nEl numero que falta es: {p} \n")

############ INCISO 2 ############################

# Metodo que encuentra el numero repetido y los numeros faltantes 
# en un arreglo cuyos valores estan entre 0 y n-1
# con complejidad O(n) y espacio extra O(1).     
def encuentraRPyS(arreglo):
    n = len(arreglo)
    r = 0
    p = 0
    s = 0
    
    for i in range(0, n):
        while arreglo[i] != arreglo[arreglo[i]]:
            tmp = arreglo[i]
            arreglo[i] = arreglo[tmp]
            arreglo[tmp] = tmp

    for i in range(0, n):
        if arreglo[i] != i and r == 0:
            p = i
            r = arreglo[i]
            continue
        if arreglo[i] != i:
            s = i
            r = arreglo[i]
            break

    print(f"\nEl numero repetido es: {r} \nLos numeros que faltan son: {p} y {s} \n")

############### INCISO 3 ####################

def ejercicio3(arr:list) -> list:

    faltantes = list()
    
    # Iterador
    i = 0
    # Cantidad de elementos
    n = len(arr)

    # Variable auxiliar para hacer el swap
    swap = -1
    # print(arr)
    while i < n:

        # Elemento en la posicion actual
        elem = arr[i]

        # Si el elemento es un pivote de repeticion o ya esta ordenado
        if (elem == -2) or (elem == i):
            i+=1
            continue

        # Veamos si se repite
        if elem == arr[elem]:
            # Dejamos un pivote en su posicion correspondiente
            arr[elem] = -2 
            # Dejamos un pivote en la posicion actual
            arr[i] = -1
            i+=1
        # En caso contrario son elementos distintos
        else: 
            # Verificamos si ya sabiamos que estaba repetido
            if arr[elem] == -2:
                arr[i] = -1
                i+=1
            # En caso contrario hacemos el swap
            else:
                swap = arr[elem]
                arr[elem] = arr[i]
                arr[i] = swap
                # Verificamos si el swap fue con un pivote
                if swap == -1:
                    i+=1

    # Determinamos los numeros repetidos y los faltantes
    for j in range(n):
        valor = arr[j]
        if valor == -1:
            faltantes.append(j)
        elif valor == -2:
            print(j)

    print(faltantes)

################# INCISO 4 ########################

def ejercicio4(arr: list) -> list:

    """
        Funcion que regresa el conjunto 
        de números repetidos y faltantes.

        Args: 
            arr: Arreglo de numeros. Los numeros solo pueden ser
                 de 0 to (n-1) con n igual a la longitud del arrego.
                 El arreglo no necesariamente tiene que estar ordenado

        Nota: Para la implementacion de este algoritmo el resultado 
        se encuentra en T(n) = O(n) con espacio O(k + m) con m la cantidad
        de numeros repetidos y k la cantidad de numeros faltantes. Ademas

            -2 = pivote de numero repetido \n
            -1 = pivote de numero faltante 

    """

    resultado = list()

    repetidos = list()

    faltantes = list()

    # Iterador
    i = 0
    # Cantidad de elementos
    n = len(arr)

    # Variable auxiliar para hacer el swap
    swap = -1
    # print(arr)
    while i < n:

        # Elemento en la posicion actual
        elem = arr[i]

        # Si el elemento es un pivote de repeticion o ya esta ordenado
        if (elem == -2) or (elem == i):
            i+=1
            continue

        # Veamos si se repite
        if elem == arr[elem]:
            # Dejamos un pivote en su posicion correspondiente
            arr[elem] = -2 
            # Dejamos un pivote en la posicion actual
            arr[i] = -1
            i+=1
        # En caso contrario son elementos distintos
        else: 
            # Verificamos si ya sabiamos que estaba repetido
            if arr[elem] == -2:
                arr[i] = -1
                i+=1
            # En caso contrario hacemos el swap
            else:
                swap = arr[elem]
                arr[elem] = arr[i]
                arr[i] = swap
                # Verificamos si el swap fue con un pivote
                if swap == -1:
                    i+=1

        # print(arr)

    # Determinamos los numeros repetidos y los faltantes
    for j in range(n):
        valor = arr[j]
        if valor == -1:
            faltantes.append(j)
        elif valor == -2:
            repetidos.append(j)

    print(repetidos)
    print(faltantes)
    
arreglo = [7,1,5,0,3,4,7,2]
# arreglo = [7,1,5,0,7,4,7,2]
# arreglo = [7,7,7,7,6,6,1,7]
# arreglo = [7,1,5,7,7,4,7,2]

ejercicio3(arreglo)
ejercicio4(arreglo)

