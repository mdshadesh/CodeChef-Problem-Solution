t = int(input())

for _ in range(t):
    n = int(input())
    coefficients = list(map(int, input().split()))
    
    degree = len(coefficients) - 1
    
    while degree > 0 and coefficients[degree] == 0:
        degree -= 1
    
    print(degree)
