t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=2*x
    z1=5*y
    if(z>z1):
        print("Chocolate")
    elif(z<z1):
        print("Candy")
    else:
        print("Either")
    
