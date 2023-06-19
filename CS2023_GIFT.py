x, n, m = map(int, input().split())

max_amount = x + m

if max_amount >= n:
    print("YES")
else:
    print("NO")
