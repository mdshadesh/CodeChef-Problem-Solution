# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the scores for each section
    a, b, c = map(int, input().split())

    # Check the conditions for passing the exam
    if a >= 10 and b >= 10 and c >= 10 and a + b + c >= 100:
        print("PASS")
    else:
        print("FAIL")
