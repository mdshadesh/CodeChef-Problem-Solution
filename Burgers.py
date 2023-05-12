# cook your dish here

# read the number of test cases
t = int(input())

# iterate through all test cases
for i in range(t):
    # read the number of patties and buns
    a, b = map(int, input().split())

    # find the maximum number of burgers
    max_burgers = min(a, b) // 1

    # print the result
    print(max_burgers)
