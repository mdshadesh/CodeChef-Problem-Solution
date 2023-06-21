T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the value of X
    X = int(input())
    
    # Determine the badge based on the number of donations
    if X <= 3:
        badge = "BRONZE"
    elif X <= 6:
        badge = "SILVER"
    else:
        badge = "GOLD"
    
    print(badge)
