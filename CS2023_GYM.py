t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    min_votes = (m // 2) + 1

    print(min_votes)
