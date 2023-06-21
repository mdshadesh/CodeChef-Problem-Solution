for i in range(int(input())):
    x,y=map(int,input().split())
    if(x>=y):
        print(y)
    else:
        print(x+(y-x)*2)