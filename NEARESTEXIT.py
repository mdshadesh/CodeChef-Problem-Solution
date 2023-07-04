# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the seat number
    seat = int(input())

    # Calculate the distance to the left exit (exit 1) and the right exit (exit 100)
    distance_left = seat - 1
    distance_right = 100 - seat

    # Choose the exit based on the minimum distance
    if distance_left <= distance_right:
        print("LEFT")
    else:
        print("RIGHT")
