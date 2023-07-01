for _ in range(int(input())):
    x, y, z = map(int, input().split())
    t = y // x
    if z > t:
        print(z - t)
    else:
        print(0)
