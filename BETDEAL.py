t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    a= 100-(100*a)/100
    b=200-(200*b)/100
    if(a>b):
        print('second')
    elif(a<b):
        print('first')
    else:
        print('both')