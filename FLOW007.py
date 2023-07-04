# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number
    n = int(input())

    # Reverse the number using string manipulation
    reversed_n = str(n)[::-1]

    # Print the reversed number
    print(int(reversed_n))
