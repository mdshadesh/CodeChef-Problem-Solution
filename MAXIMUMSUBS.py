# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the contest duration in minutes
    x = int(input())

    # Convert minutes to seconds
    duration_seconds = x * 60

    # Calculate the maximum number of submissions
    submissions = (duration_seconds // 30) - (duration_seconds % 30 >= 5)

    # Print the result
    print(submissions)
