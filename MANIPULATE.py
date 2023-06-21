# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read X and Y for each test case
    X, Y = map(int, input().split())

    # Check if Ezio can manipulate all the guards
    if Y <= X:
        print("YES")
    else:
        print("NO")

