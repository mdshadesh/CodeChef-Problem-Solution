T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the values of X, Y, and Z
    X, Y, Z = map(int, input().split())

    # Calculate the total number of seats available
    total_seats = X * 10

    # Calculate the maximum number of people that can book a seat
    max_people = min(total_seats, Y)

    # Calculate the maximum amount that Chef can earn
    max_earnings = max_people * Z

    # Print the maximum earnings
    print(max_earnings)
