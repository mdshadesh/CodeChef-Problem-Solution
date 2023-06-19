t = int(input())
for _ in range(t):
    x, p, q = map(int, input().split())
    fine = max(0, p - q) * x
    print(fine)
