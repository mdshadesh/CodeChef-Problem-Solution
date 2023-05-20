# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of K and X
    K, X = map(int, input().split())
    
    # Calculate the remaining days Chef has to wait
    remaining_days = (K * 7) - X
    
    # If the remaining days is a multiple of 7, subtract 7 to get the minimum remaining days
    if remaining_days % 7 == 0:
        remaining_days -= 7
    
    # Print the number of remaining days
    print(remaining_days)
