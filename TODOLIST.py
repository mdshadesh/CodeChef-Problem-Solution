def remove_problems(num_problems, ratings):
    count = 0
    for rating in ratings:
        if rating >= 1000:
            count += 1
    return count

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of problems
    num_problems = int(input())
    # Read the difficulty ratings
    ratings = list(map(int, input().split()))

    # Calculate the number of problems to remove
    result = remove_problems(num_problems, ratings)

    # Print the result
    print(result)
