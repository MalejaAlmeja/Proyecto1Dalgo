def problema(arr, m, j):
    n=len(arr)
    temporal_menor = []
    valor_min=float("inf")
    arr=arr[0:m+j]
    arreglo_subarreglos= hacer_subarreglos_j(arr, j)
    for subarray in arreglo_subarreglos:
            if posible(arr, subarray) and sum(subarray)<valor_min:
                temporal_menor=subarray
                valor_min=sum(temporal_menor)

    return valor_min

def posible(arr, caso):
    posible = False
    #Terminar
    return posible

def hacer_subarreglos_j(arr, j):
    def backtrack(start, path):
        if len(path) == j:
            resultado.append(path[:])  # Copiamos la lista actual y la guardamos
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()  # Deshacemos la elección para probar otra combinación

    resultado = []
    backtrack(0, [])
    print(resultado)
    return resultado

import time

def find_minimum_weight_sum_dp(weights, group_size, max_swaps):
    n = len(weights)
    INF = float('inf')

    # Initialize 3D DP table: dp[i][k][s]
    # i = players considered
    # k = players selected
    # s = total swaps used
    dp = [[[INF] * (max_swaps + 1) for _ in range(group_size + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0  # base case: 0 players, 0 selected, 0 swaps

    for i in range(n):  # for each player
        for selected in range(group_size + 1):
            for swaps in range(max_swaps + 1):
                if dp[i][selected][swaps] == INF:
                    continue

                # Option 1: skip this player
                dp[i + 1][selected][swaps] = min(dp[i + 1][selected][swaps], dp[i][selected][swaps])

                # Option 2: select this player (if room in group)
                if selected < group_size:
                    cost_to_move = i - selected
                    new_swap_total = swaps + cost_to_move
                    if new_swap_total <= max_swaps:
                        dp[i + 1][selected + 1][new_swap_total] = min(
                            dp[i + 1][selected + 1][new_swap_total],
                            dp[i][selected][swaps] + weights[i]
                        )

    # Get minimum result for selecting `group_size` players using any swaps ≤ max_swaps
    return min(dp[n][group_size][s] for s in range(max_swaps + 1))

# Inicia el cronómetro
start_time = time.time()

test_cases = [
    [5, 2, 3, 3, 1, 4, 2, 5],
    [8, 3, 6, 57, 43, 31, 21, 13, 1, 7, 3],
    [13, 7, 20, 57, 27, 13, 91, 73, 1, 13, 1, 43, 21, 31, 3, 7],
    [17, 2, 2, 43, 81, 103, 13, 27, 61, 43, 31, 21, 13, 1, 7, 1, 3, 91, 73, 57],
    [23, 11, 19, 127, 103, 1, 23, 81, 43, 61, 153, 181, 47, 7, 3, 27, 91, 43, 57, 21, 1, 73, 13, 13, 1, 31]
]

for idx, case in enumerate(test_cases, 1):
    n = case[0]
    j = case[1]
    m = case[2]
    weights = case[3:]
    result = find_minimum_weight_sum_dp(weights, j, m)
    print(f"Case #{idx}: Minimum total weight of first {j} players = {result}")

# Detiene el cronómetro
end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTiempo total de ejecución: {elapsed_time:.4f} segundos")

print("//////////////////////////////////////////////////////////////////////////////////")

def find_minimum_weight_sum_dp_optimized(weights, group_size, max_swaps):
    n = len(weights)
    INF = float('inf')

    # dp[selected][swaps] = minimum total weight for this state
    dp = [[INF] * (max_swaps + 1) for _ in range(group_size + 1)]
    dp[0][0] = 0  # Base case: 0 players selected, 0 swaps used

    for i in range(n):  # for each player
        # Use a copy to preserve previous state while updating
        new_dp = [row[:] for row in dp]

        for selected in range(group_size):
            for swaps in range(max_swaps + 1):
                if dp[selected][swaps] == INF:
                    continue

                cost_to_move = i - selected
                total_swaps = swaps + cost_to_move

                if total_swaps <= max_swaps:
                    new_weight = dp[selected][swaps] + weights[i]
                    new_dp[selected + 1][total_swaps] = min(
                        new_dp[selected + 1][total_swaps], new_weight
                    )

        dp = new_dp  # Move to next player

    return min(dp[group_size][s] for s in range(max_swaps + 1))

test_cases = [
    [5, 2, 3, 3, 1, 4, 2, 5],
    [8, 3, 6, 57, 43, 31, 21, 13, 1, 7, 3],
    [13, 7, 20, 57, 27, 13, 91, 73, 1, 13, 1, 43, 21, 31, 3, 7],
    [17, 2, 2, 43, 81, 103, 13, 27, 61, 43, 31, 21, 13, 1, 7, 1, 3, 91, 73, 57],
    [23, 11, 19, 127, 103, 1, 23, 81, 43, 61, 153, 181, 47, 7, 3, 27, 91, 43, 57, 21, 1, 73, 13, 13, 1, 31]
]

for idx, case in enumerate(test_cases, 1):
    n = case[0]
    j = case[1]
    m = case[2]
    weights = case[3:]
    result = find_minimum_weight_sum_dp_optimized(weights, j, m)
    print(f"Case #{idx}: Minimum total weight of first {j} players = {result}")
    
# Detiene el cronómetro
end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTiempo total de ejecución: {elapsed_time:.4f} segundos")