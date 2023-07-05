for _ in range(int(input())):
    n,a,b=map(int,input().split())
    s=input()
    x=0
    y=0
    
    for i in range(n):
        x=s.count('0')
        y=s.count('1')
        
    print(a*x + b*y)