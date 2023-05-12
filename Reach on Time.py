def can_chef_reach_on_time(x):
    if x >= 30:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
    # Read the value of X
    x = int(input())

    # Determine if Chef can reach on time
    result = can_chef_reach_on_time(x)

    # Print the result
    print(result)
