t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    
    max_filled_bottles = min(k // x, n)
    
    print(max_filled_bottles)
