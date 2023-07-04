def solve():
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(b):
        sum += arr[i]
    total = (a * (a + 1)) // 2
    print(total - sum)


t = int(input())
for _ in range(t):
    solve()
