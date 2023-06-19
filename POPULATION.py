t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    population = x - y + z
    print(population)
