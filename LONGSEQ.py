def can_make_equal(num):
    count_0 = num.count('0')
    count_1 = num.count('1')
    
    if count_0 == 1 or count_1 == 1:
        return "Yes"
    
    if count_0 == 0 or count_1 == 0:
        return "No"
    
    return "No"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    num = input().strip()
    result = can_make_equal(num)
    print(result)
