T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the revenues of the three companies
    R1, R2, R3 = map(int, input().split())

    # Check if any company has a monopolistic advantage
    if R1 > R2 + R3 or R2 > R1 + R3 or R3 > R1 + R2:
        print("YES")
    else:
        print("NO")
