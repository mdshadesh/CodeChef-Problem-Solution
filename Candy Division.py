# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of candies
    N = int(input())
    
    # Check if the candies can be distributed equally
    if N % 3 == 0:
        print("YES")
    else:
        print("NO")
