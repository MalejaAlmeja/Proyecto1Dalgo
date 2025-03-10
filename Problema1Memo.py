def find_minimum_weight_sum_memo(weights, group_size, max_swaps):
    total_players = len(weights)
    memo = {}

    def dp(current_index, selected_count, swap_cost):
        # Check if result already memoized
        key = (current_index, selected_count, swap_cost)
        if key in memo:
            return memo[key]

        # Base Case: selected enough players
        if selected_count == group_size:
            return 0  # no more weight to add

        # Base Case: ran out of players
        if current_index >= total_players:
            return float('inf')

        # Option 1: Skip current player
        option_skip = dp(current_index + 1, selected_count, swap_cost)

        # Option 2: Include current player
        cost_to_move = current_index - selected_count
        option_take = float('inf')
        if swap_cost + cost_to_move <= max_swaps:
            option_take = weights[current_index] + dp(current_index + 1, selected_count + 1, swap_cost + cost_to_move)

        # Store the result in memo table
        memo[key] = min(option_skip, option_take)
        return memo[key]

    return dp(0, 0, 0)


# Test cases
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
    result = find_minimum_weight_sum_memo(weights, j, m)
    print(f"Case #{idx}: Minimum total weight of first {j} players = {result}")