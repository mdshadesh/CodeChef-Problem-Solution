def check_qualification(T):
    for _ in range(T):
        X, Y = map(int, input().split())
        qualifying_time = X * 1.07
        if Y <= qualifying_time:
            print("YES")
        else:
            print("NO")

T = int(input())
check_qualification(T)
