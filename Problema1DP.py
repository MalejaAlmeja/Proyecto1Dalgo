## Grupo de 3 conformado por:
# María Alejandra Carrillo: 202321854
# Juan David Uribe: 202322433
# Raúl Sebastián Ruiz: 202321332
import sys
import time
def algormar_dp(pesos, n, j, m):
    INF = float('inf')
    
    # Inicializar tabla 3D DP: dp[i][k][s]
    # i = jugadores considerados
    # k = jugadores seleccionados
    # s = swaps usados
    
    dp = [[[INF] * (m + 1) for _ in range(j + 1)] for _ in range(n + 1)]
    
    # Caso base: 0 jugadores, 0 seleccionados, 0 swaps
    dp[0][0][0] = 0

    for i in range(n):  # Para cada jugador
        for seleccionado in range(j + 1):
            for swaps in range(m + 1):
                if dp[i][seleccionado][swaps] == INF:
                    continue

                # Opción 1: No incluir jugador actual
                dp[i + 1][seleccionado][swaps] = min(dp[i + 1][seleccionado][swaps], dp[i][seleccionado][swaps])

                # Opción 2: Seleccionar este jugador (si hay espacio en el grupo)
                if seleccionado < j:
                    costo_mover = i - seleccionado
                    nuevo_swap_total = swaps + costo_mover
                    if nuevo_swap_total <= m:
                        dp[i + 1][seleccionado + 1][nuevo_swap_total] = min(
                            dp[i + 1][seleccionado + 1][nuevo_swap_total],
                            dp[i][seleccionado][swaps] + pesos[i]
                        )

    # Caso final: Obtener el mínimo resultado para seleccionar `j` jugadores usando cualquier swap ≤ m
    return min(dp[n][j][s] for s in range(m + 1))


# # Casos de estudio
# casos_estudio = [
#     [5, 2, 3, 3, 1, 4, 2, 5],
#     [8, 3, 6, 57, 43, 31, 21, 13, 1, 7, 3],
#     [13, 7, 20, 57, 27, 13, 91, 73, 1, 13, 1, 43, 21, 31, 3, 7],
#     [17, 2, 2, 43, 81, 103, 13, 27, 61, 43, 31, 21, 13, 1, 7, 1, 3, 91, 73, 57],
#     [23, 11, 19, 127, 103, 1, 23, 81, 43, 61, 153, 181, 47, 7, 3, 27, 91, 43, 57, 21, 1, 73, 13, 13, 1, 31]
# ]

# for indice, caso in enumerate(casos_estudio, 1):
#     n = caso[0]
#     j = caso[1]
#     m = caso[2]
#     pesos = caso[3:]
#     start = time.time()
#     resultado = algormar_dp(pesos, n, j, m)
#     end = time.time()
#     print(f"Caso #{indice}: Peso minimo total de los primeros {j} jugadores = {resultado}")
#     print("Tiempo de ejecución: ",end - start)
    
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
        print(algormar_dp(pesos, n, j, m))
        linea = sys.stdin.readline()
main()