## Grupo de 3 conformado por:
# María Alejandra Carrillo: 202321854
# Juan David Uribe: 202322433
# Raúl Sebastián Ruiz: 202321332
import sys
def algormar_memorizacion(pesos, n, j, m):
    memoria = {}

    def dp(indice_actual, cuenta_seleccionada, costo_swap):
        # Revisa si el resultado ha sido memorizado
        llave = (indice_actual, cuenta_seleccionada, costo_swap)
        if llave in memoria:
            return memoria[llave]

        # Caso base: Se seleccionan suficientes jugadores
        if cuenta_seleccionada == j:
            return 0  # No hay que agregar peso

        # Caso base: Nos quedamos sin jugadores
        if indice_actual >= n:
            return float('inf')

        # Opción 1: No incluir jugador actual
        skip = dp(indice_actual + 1, cuenta_seleccionada, costo_swap)

        # Optción 2: Incluir jugador actual
        costo_mover = indice_actual - cuenta_seleccionada
        tomar = float('inf')
        if costo_swap + costo_mover <= m:
            tomar = pesos[indice_actual] + dp(indice_actual + 1, cuenta_seleccionada + 1, costo_swap + costo_mover)

        # Guarda el resultado en la memoria
        memoria[llave] = min(skip, tomar)
        return memoria[llave]

    return dp(0, 0, 0)

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
        print(algormar_memorizacion(pesos, n, j, m))
        linea = sys.stdin.readline()
main()