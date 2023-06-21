# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the values for N and M
    n, m = map(int, input().split())

    # Calculate the total number of bike and car tyres
    bike_tyres = n * 2
    car_tyres = m * 4

    # Calculate the total number of tyres on the road
    total_tyres = bike_tyres + car_tyres

    # Print the result
    print(total_tyres)
