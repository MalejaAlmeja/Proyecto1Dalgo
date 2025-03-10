## Grupo de 3 conformado por:
# María Alejandra Carrillo: 202321854
# Juan David Uribe: 202322433
# Raúl Sebastián Ruiz: 202321332
import sys
def calcular_costo_swap(indices):
    costo = 0
    for i in range(len(indices)):
        costo += indices[i] - i # cuandos elementos necesitan ser pasados
    return costo

def combinaciones(pesos, n, j, m, inicio, camino, min_peso):
    if len(camino) == j:
        # Tenemos la subsecuencia de longitud j, la evaluamos
        costo_swap = calcular_costo_swap(camino)
        if costo_swap <= m:
            peso_total = sum(pesos[i] for i in camino)
            min_peso[0] = min(min_peso[0], peso_total)
        return
    for i in range(inicio, n):
        combinaciones(pesos, n, j, m, i + 1, camino + [i], min_peso)


def algormar_recursivo(pesos, n, j, m):
    min_peso = [float('inf')]
    combinaciones(pesos, n, j, m, 0, [], min_peso)
    return min_peso[0]

"""
# Casos de estudio
casos_estudio = [
    [5, 2, 3, 3, 1, 4, 2, 5],
    [8, 3, 6, 57, 43, 31, 21, 13, 1, 7, 3],
    [13, 7, 20, 57, 27, 13, 91, 73, 1, 13, 1, 43, 21, 31, 3, 7],
    [17, 2, 2, 43, 81, 103, 13, 27, 61, 43, 31, 21, 13, 1, 7, 1, 3, 91, 73, 57],
    [23, 11, 19, 127, 103, 1, 23, 81, 43, 61, 153, 181, 47, 7, 3, 27, 91, 43, 57, 21, 1, 73, 13, 13, 1, 31]
]

for indice, caso in enumerate(casos_estudio, 1):
    n = caso[0]
    j = caso[1]
    m = caso[2]
    pesos = caso[3:]
    resultado = algormar_recursivo(pesos,n, j, m)
    print(f"Caso #{indice}: Peso minimo total de los primeros {j} jugadores = {resultado}")
"""

def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,ncasos):
        numeros = [int(num) for num in linea.split()]
        n = numeros[0]
        j = numeros[1]
        m = numeros[2]
        pesos = numeros[3:]
        print(algormar_recursivo(pesos, n, j, m))
        linea = sys.stdin.readline()
    
main()