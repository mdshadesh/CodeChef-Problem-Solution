for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=[]
    b=[]
    
    for i in range(n):
        if i%2!=0:
            a.append(x[i])
            b.append(y[i])
        else:
            a.append(y[i])
            b.append(x[i])
    print(min(sum(a),sum(b)))
        