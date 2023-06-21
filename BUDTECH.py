# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the budget of Technex'23
    n = int(input())

    # Calculate the maximum amount in rupees that could be allocated to each of the other five events
    max_allocation = n * 100

    # Print the result
    print(max_allocation)
