for i in range(int(input())):
    x,y = map(int,input().split())
    x += y 
    if(x>=7):
        print("yes")
    else:
        print("no")