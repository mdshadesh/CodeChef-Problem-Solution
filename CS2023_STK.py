t = int(input())

for _ in range(t):
    n = int(input())
    om = list(map(int, input().split()))
    addy = list(map(int, input().split()))

    max_om_streak = 0
    max_addy_streak = 0
    om_streak = 0
    addy_streak = 0

    for i in range(n):
        if om[i] > 0:
            om_streak += 1
            max_om_streak = max(max_om_streak, om_streak)
        else:
            om_streak = 0

        if addy[i] > 0:
            addy_streak += 1
            max_addy_streak = max(max_addy_streak, addy_streak)
        else:
            addy_streak = 0

    if max_om_streak > max_addy_streak:
        print("OM")
    elif max_om_streak < max_addy_streak:
        print("ADDY")
    else:
        print("DRAW")
