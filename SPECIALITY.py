# cook your dish here
# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the counts of problems set, tested, and written editorials for
    x, y, z = map(int, input().split())

    # Compare the counts and determine the most active role
    if x > y and x > z:
        print("SETTER")
    elif y > x and y > z:
        print("TESTER")
    else:
        print("EDITORIALIST")
