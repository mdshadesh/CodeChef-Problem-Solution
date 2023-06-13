T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())

    if X * Y >= N:
        print("YES")
    else:
        print("NO")
