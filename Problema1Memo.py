## Grupo de 3 conformado por:
# María Alejandra Carrillo: 202321854
# Juan David Uribe: 202322433
# Raúl Sebastián Ruiz: 202321332

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
    resultado = algormar_memorizacion(pesos, n, j, m)
    print(f"Caso #{indice}: Peso minimo total de los primeros {j} jugadores = {resultado}")