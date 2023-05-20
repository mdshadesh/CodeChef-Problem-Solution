# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of A, B, and C
    A, B, C = map(int, input().split())
    
    # Check if the sum of A and B equals C
    if A + B == C:
        print("YES")
    else:
        print("NO")
