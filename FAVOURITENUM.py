T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the value of A
    A = int(input())

    # Check if A is even and a multiple of 7
    if A % 2 == 0 and A % 7 == 0:
        print("Alice")
    # Check if A is odd and a multiple of 9
    elif A % 2 == 1 and A % 9 == 0:
        print("Bob")
    # If neither condition is satisfied
    else:
        print("Charlie")
