# cook your dish here


t = int(input())  # read the number of test cases

for i in range(t):
    x, y = map(int, input().split())  # read X and Y for each test case
    total_cost = x * y  # calculate the total cost
    print(total_cost)  # print the result for each test case
