# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read X and Y for each test case
    X, Y = map(int, input().split())

    # Calculate the total amount Chef made
    total_amount = X + max(0, Y - X) * 2

    # Print the total amount
    print(total_amount)
