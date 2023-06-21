# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the lengths of the sides of the triangle
    a, b, c = map(int, input().split())

    # Check if the triangle is scalene
    if a != b and b != c and c != a:
        print("YES")
    else:
        print("NO")
