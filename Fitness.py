# Number of test cases
t = int(input())

for i in range(t):
    # Distance between home and office
    x = int(input())
    
    # Total distance traveled in a week (to and from office)
    total_distance = 2 * x * 5
    
    print(total_distance)
