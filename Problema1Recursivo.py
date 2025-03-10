def calculate_swap_cost(indices):
    cost = 0
    positions = sorted(indices)  # where the elements currently are
    for i in range(len(positions)):
        cost += positions[i] - i  # how many elements need to be passed over
    return cost


def dfs(weights, n, j, m, start, path, min_weight):
    if len(path) == j:
        # We have a full subsequence of length j, evaluate it
        swap_cost = calculate_swap_cost(path)
        if swap_cost <= m:
            total_weight = sum(weights[i] for i in path)
            min_weight[0] = min(min_weight[0], total_weight)
        return
    
    for i in range(start, n):
        dfs(weights, n, j, m, i + 1, path + [i], min_weight)


def find_min_total_weight(weights, j, m):
    n = len(weights)
    min_weight = [float('inf')]
    dfs(weights, n, j, m, 0, [], min_weight)
    return min_weight[0]

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
    result = find_min_total_weight(weights, j, m)
    print(f"Case #{idx}: Minimum total weight of first {j} players = {result}")