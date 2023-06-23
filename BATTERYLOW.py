T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the battery level
    X = int(input())

    # Check if the battery level is <= 15%
    if X <= 15:
        print("Yes")
    else:
        print("No")
