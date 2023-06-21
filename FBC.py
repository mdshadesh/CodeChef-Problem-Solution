t = int(input())

for _ in range(t):
    k, x = map(int, input().split())
    extra_water = k - x
    print(extra_water)
