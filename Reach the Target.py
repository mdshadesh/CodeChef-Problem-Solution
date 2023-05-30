# cook your dish here

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    remaining_runs = x - y
    print(remaining_runs)
