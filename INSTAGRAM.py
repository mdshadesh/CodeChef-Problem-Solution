t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if x <= 10 * y:
        print("NO")
    else:
        print("YES")
