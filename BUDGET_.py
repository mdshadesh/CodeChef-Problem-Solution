# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the amount of money Akshat has and his daily expenditure
    x, y = map(int, input().split())
    
    # Calculate the total expenditure for the month
    total_expenditure = y * 30
    
    # Check if Akshat has enough money for the entire month
    if x >= total_expenditure:
        print("YES")
    else:
        print("NO")
