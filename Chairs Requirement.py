# cook your dish here
T = int(input())
for i in range(T):
    X, Y = map(int, input().split())
    if Y>X:
        print(0)
    else:
        print(X-Y)