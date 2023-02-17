
# ANALISIS DE ALGORITMOS
# Semanal 3
# Arrieta Mancera Luis Sebastian
# Martinez Hernandez Zuriel ENrique (318056423)

# Metodo que encuentra el numero faltante en un arreglo 
# cuyos valores estan entre entre 0 y n − 1.
def numeroFaltante(arreglo):
    n = len(arreglo)
    total = ((n-1) + 1)*(((n-1) + 2)/2)
    suma = sum(arreglo)
    return int(total - suma)

# Metodo que encuentra el numero repetido en un arreglo
# cuyos valores estan entre entre 0 y n − 1.
def numeroRepetido(arreglo):
    visitado = set()
    duplicado = [x for x in arreglo if x in visitado or (visitado.add(x) or False)]
    repetido = duplicado[0]
    return repetido
    
# Metodo que encuentra el numero repetido y el numnero faltante 
# en un arreglo cuyos valores estan entre entre 0 y n − 1.
# con complejidad O(n) y espacio extra O(n)
def encuentraRyP(arreglo):
    r = numeroRepetido(arreglo)
    arreglo.remove(r)
    p = numeroFaltante(arreglo)
    print(f"\nEl numero repetido es: {r} \nEl numero que falta es: {p} \n")


arreglo = [6, 1, 3, 0, 4, 3, 2]

print(encuentraRyP(arreglo))
