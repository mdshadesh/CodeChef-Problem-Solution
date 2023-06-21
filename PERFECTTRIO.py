# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the ages of the three members of the group
    a, b, c = map(int, input().split())

    # Check if the group is perfect
    if a == b + c or b == a + c or c == a + b:
        print("YES")
    else:
        print("NO")
