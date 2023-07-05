for _ in range(int(input())):
    l=list(map(int,input().split()))
    l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=input()
    s1=0
    for i in range(26):
        if(l1[i] not in s):
            s1+=l[i]
    print(s1)        
            
                