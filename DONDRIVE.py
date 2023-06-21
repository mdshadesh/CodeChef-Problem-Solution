T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of N and X
    N, X = map(int, input().split())
    
    # Calculate the remaining number of donations needed
    remaining = N - X
    
    print(remaining)
