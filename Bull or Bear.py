# cook your dish here
t= int(input())
for i in range(t):
    l=list(map(int,input().split()))
    if(l[0]>l[1]):
        print("LOSS")
    elif(l[0]==l[1]):
        print("NEUTRAL")
    else:
        print("PROFIT")
        
        
    
