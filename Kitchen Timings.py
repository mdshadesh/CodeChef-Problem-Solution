t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    if y < x:
        y += 12
    print(y - x)
