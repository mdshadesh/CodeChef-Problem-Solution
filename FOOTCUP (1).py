# cook your dish here
t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    if(a==0 and b==0):
        print('no')
    elif(a == b ):
        print('yes')
    else:
        print('no')