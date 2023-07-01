for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    moved = []
    unmoved = []
    for i in range(n):
        if i+k <= n-1 or i >= k: moved.append(a[i])
        else: unmoved.append(a[i])
    moved.sort()
    if not unmoved: print(*moved)
    else:
        k = len(moved)
        ans = moved[:k//2] + unmoved + moved[k//2:]
        print(*ans)