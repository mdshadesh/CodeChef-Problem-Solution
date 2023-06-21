# Read the number of problems solved in each week
p1, p2, p3, p4 = map(int, input().split())

# Initialize a counter variable to count the number of weeks Chef met the target
count = 0

# Check if the number of problems solved in each week is at least 10
if p1 >= 10:
    count += 1
if p2 >= 10:
    count += 1
if p3 >= 10:
    count += 1
if p4 >= 10:
    count += 1

# Print the number of weeks Chef met the target
print(count)
