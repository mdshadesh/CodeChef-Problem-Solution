t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    if k >= (n * x):
        print("YES")
    else:
        print("NO")
