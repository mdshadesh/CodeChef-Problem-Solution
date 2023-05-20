# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the free space in computer, number of 1GB files, and number of 2GB files
    N, X, Y = map(int, input().split())
    
    # Calculate the total size of files
    total_size = X + 2 * Y
    
    # Check if Chef is able to save the files
    if total_size <= N:
        print("YES")
    else:
        print("NO")
