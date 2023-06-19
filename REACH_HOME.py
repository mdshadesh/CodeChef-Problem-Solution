T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    max_distance = X * 5  # Maximum distance with X litres of fuel
    if max_distance >= Y:
        print("YES")
    else:
        print("NO")
