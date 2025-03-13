import sys

# Programa para calcular el peso mínimo total de jugadores seleccionados
# bajo la restricción de cantidad máxima de intercambios (swaps)

## ESTE ES EL INTENTO DE 2D DE CHAT

def algormar_dp(pesos, n, j, m):
    INF = float('inf')
    dp = [[INF] * (m + 1) for _ in range(j + 1)]
    dp[0][0] = 0

    for i in range(n):
        peso_actual = pesos[i]
        # Hacemos copia del dp para esta ronda
        dp_ant = [fila[:] for fila in dp]

        for seleccionados in range(j + 1):
            for swaps in range(m + 1):
                if dp_ant[seleccionados][swaps] == INF:
                    continue
                # Opción 1: no seleccionar al jugador i (no cambia nada)
                dp[seleccionados][swaps] = min(dp[seleccionados][swaps], dp_ant[seleccionados][swaps])

                # Opción 2: seleccionarlo (si no superamos j ni m)
                if seleccionados < j:
                    costo_mover = i - seleccionados
                    total_swaps = swaps + costo_mover
                    if total_swaps <= m:
                        dp[seleccionados + 1][total_swaps] = min(
                            dp[seleccionados + 1][total_swaps],
                            dp_ant[seleccionados][swaps] + peso_actual
                        )

    return min(dp[j][s] for s in range(m + 1) if dp[j][s] != INF)


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