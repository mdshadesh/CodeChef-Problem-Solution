# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the cost of getting the phone repaired and the cost of buying a new phone
    x, y = map(int, input().split())

    # Compare the costs and print the result
    if x < y:
        print("REPAIR")
    elif x > y:
        print("NEW PHONE")
    else:
        print("ANY")
