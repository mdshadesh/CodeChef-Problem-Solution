# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the inputs
    n, m, k = map(int, input().split())

    # Check if Eikooc can eat all the loaves before they expire
    if k * m >= n:
        print("Yes")
    else:
        print("No")
