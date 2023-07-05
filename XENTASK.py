T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    min_time = float('inf')
    
    for i in range(N):
        time = max(sum(X[:i+1]), sum(Y[i:]))
        min_time = min(min_time, time)
    
    print(min_time)
