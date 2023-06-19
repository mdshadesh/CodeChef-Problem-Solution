T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    cost_double = 3 * X  # Cost of three double rooms
    cost_triple = 2 * Y  # Cost of two triple rooms
    min_cost = min(cost_double, cost_triple)
    print(min_cost)
