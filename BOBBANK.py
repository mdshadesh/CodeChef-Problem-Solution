T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the inputs
    W, X, Y, Z = map(int, input().split())

    # Calculate the final balance
    final_balance = W + (X - Y) * Z

    # Print the final balance
    print(final_balance)
