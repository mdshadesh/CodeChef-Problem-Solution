t = int(input())

for i in range(t):
    x, n = map(int, input().split())
    score = n * (x // 10)
    print(score)
