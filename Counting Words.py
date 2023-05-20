# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of pages and words per page
    N, M = map(int, input().split())
    
    # Calculate the total number of words
    total_words = N * M
    
    # Print the result
    print(total_words)
