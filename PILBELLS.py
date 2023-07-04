def solve():
    n, x, k, p = map(int, input().split())
    if n == k:
        add = p + 20
    else:
        add = p
    cnt = 0
    if k == 0:
        print(p)
    else:
        while k > 0:
            if x > 0:
                add += 10
                x -= 1
            else:
                add += 5
            k -= 1
        print(add)


t = int(input())
while t > 0:
    solve()
    t -= 1
