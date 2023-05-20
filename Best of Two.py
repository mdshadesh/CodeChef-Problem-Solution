# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the marks scored in the first and second attempt
    X, Y = map(int, input().split())
    
    # Determine the final score by taking the maximum of X and Y
    final_score = max(X, Y)
    
    # Print the final score
    print(final_score)
