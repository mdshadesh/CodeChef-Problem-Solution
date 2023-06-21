# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the cost of disposable masks and cloth masks
    x, y = map(int, input().split())

    # Calculate the cost of masks for 100 days
    cost_disposable = x * 100
    cost_cloth = y * 10

    # Compare the costs and determine the choice
    if cost_disposable < cost_cloth:
        print("DISPOSABLE")
    else:
        print("CLOTH")
