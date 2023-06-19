t=int(input())
for i in  range(t):
    x,y=map(int,input().split())
    if(y>=x*3):
        print('yes')
    else:
        print('no')