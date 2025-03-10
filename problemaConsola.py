import sys

# Programa para calcular el peso mínimo total de jugadores seleccionados
# bajo la restricción de cantidad máxima de intercambios (swaps)

def algormar_dp(pesos, n, j, m):
    INF = float('inf')

    # Inicializar la tabla DP 3D: dp[i][k][s]
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

    # Resultado final: mínimo peso total posible usando swaps ≤ m
    return min(dp[n][j][s] for s in range(m + 1))


def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)

    for i in range(ncasos):
        linea = sys.stdin.readline()
        caso = list(map(int, linea.strip().split()))
        n = caso[0]
        j = caso[1]
        m = caso[2]
        pesos = caso[3:]
        print(str(algormar_dp(pesos, n, j, m)))

main()