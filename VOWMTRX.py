for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    x=input()
    m=10**9+7
    
    v="aeiou"
    cf,cb=0,n-1
    r=True
    while r:
        if x[cb] not in v:
            cb-=1
            n=n-1
        if x[cf] not in v:
            cf+=1
            n=n-1
        if x[cf] in v and x[cb] in v:
            break
    x=x[cf:cb+1]
        
    
    ans=1
    tv=0
    t=0
    for i in range(n):
        if x[i] in v :
            ans = (ans % m) * ((t + 1) % m) % m

            t=0
            tv+=1
        else :
            if tv%k==0 :
                t+=1
            
    print((ans)%m)
        