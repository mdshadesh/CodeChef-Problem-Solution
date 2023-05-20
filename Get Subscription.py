# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the duration of the lecture
    X = int(input())
    
    # Check if Chef needs to take the subscription
    if X > 30:
        print("YES")
    else:
        print("NO")
