def solve():
    a, b, c, d, e, f = map(int, input().split())
    sum1 = a + b + c
    x = min(a, b, c)
    res1 = sum1 - x

    sum2 = d + e + f
    y = min(d, e, f)
    res2 = sum2 - y

    if res1 > res2:
        print("Alice")
    elif res1 < res2:
        print("Bob")
    else:
        print("Tie")

t = int(input())
for _ in range(t):
    solve()
