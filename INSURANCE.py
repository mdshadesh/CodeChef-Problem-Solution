T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())

    # Check if the amount required is within the maximum rebatable amount
    if Y <= X:
        print(Y)
    else:
        print(X)
