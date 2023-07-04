# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the rank of Chef
    rank = int(input())

    # Calculate the page number
    page = (rank - 1) // 25 + 1

    # Print the page number
    print(page)
