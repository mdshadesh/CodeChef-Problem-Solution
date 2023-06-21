t=int(input())
for i in range(t):
    a,b=input().split()
    x=int(a)
    y=int(b)
    if(x>y):
        print(x-y)
    else:
        print(y-x)
