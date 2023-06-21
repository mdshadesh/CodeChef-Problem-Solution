T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    
    total_rupees = X * 5 + Y * 10
    max_chocolates = total_rupees // Z
    
    print(max_chocolates)
