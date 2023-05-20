# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of RTP courses, Audit courses, and Non-RTP courses
    X, Y, Z = map(int, input().split())
    
    # Calculate the total credits obtained
    total_credits = 4 * X + 2 * Y + 0 * Z
    
    # Print the result
    print(total_credits)
