t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    m = []
   
    
    for i in range(n-1):
        if l[i]!=l[i+1]:
         
            m.append(i)
            m.append(i+1)
    
    
    print(len(set(m)))

    