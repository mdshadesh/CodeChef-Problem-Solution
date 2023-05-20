# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the height of Chef's son and the minimum height required
    X, H = map(int, input().split())
    
    # Check if Chef's son can go on the ride
    if X >= H:
        print("YES")
    else:
        print("NO")
