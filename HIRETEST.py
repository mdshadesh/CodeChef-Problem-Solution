for _ in range(int(input())):
    n,m = map(int,input().split())
    x,y = map(int,input().split())
    a = ""
    for i in range(n):
        j = input()
        F = j.count('F')
        P = j.count('P')
        if F>=x or (F>=x-1 and P>=y):
            a+="1"
        else:
            a+="0"
    print(a)