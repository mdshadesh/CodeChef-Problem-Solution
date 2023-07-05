import math

T = int(input())

for _ in range(T):
    N = int(input())
    
    result = math.pow(0.143 * N, N)
    rounded_result = round(result)
    
    print(rounded_result)
