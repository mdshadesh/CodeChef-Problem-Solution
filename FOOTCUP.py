t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if x != y and (x > 0 or y > 0):
        print("YES")
    else:
        print("NO")
