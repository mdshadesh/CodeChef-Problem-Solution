T = int(input())
for _ in range(T):
    N, M, X = map(int, input().split())
    perimeter = 2 * (N + M)
    cost = perimeter * X
    print(cost)
