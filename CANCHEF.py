T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Calculate the maximum distance that can be covered
    max_distance = X * 15

    # Check if it is possible to attend the event and return home
    if max_distance >= 2 * Y:
        print("YES")
    else:
        print("NO")
