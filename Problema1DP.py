## Grupo de 3 conformado por:
# María Alejandra Carrillo: 202321854
# Juan David Uribe: 202322433
# Raúl Sebastián Ruiz: 202321332

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