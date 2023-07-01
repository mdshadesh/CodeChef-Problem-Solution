t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    # Calculate the difference in ratings
    diff = y - x

    # Calculate the minimum number of games needed to win
    games = (diff + 7) // 8

    print(games)
