for i in range(int(input())):
    a,b,c,x=map(int,input().split())
    
    if a+b>=x or b+c>=x or a+c>=x: 
        print('YES')
    else: 
        print('NO')