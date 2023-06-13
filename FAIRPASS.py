t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print("YES") if (n+1 <= k) else print("NO")