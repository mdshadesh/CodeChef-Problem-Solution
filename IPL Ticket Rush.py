t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    if n <= m:
        print(0)
    else:
        print(n - m)
