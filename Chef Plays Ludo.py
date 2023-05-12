# cook your dish here


# read the number of test cases
t = int(input())

# iterate through all test cases
for i in range(t):
    # read the rolled number
    x = int(input())

    # check if Chef can enter a new token
    if x == 6:
        print("YES")
    else:
        print("NO")
