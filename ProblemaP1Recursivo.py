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