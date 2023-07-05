T=int(input())
for i in range(T):
    n=int(input())
    lst=[int(c) for c in input().split()]
    emplst=[]
    cnt=0
    for x in lst:
        if x not in emplst:
            emplst.append(x)
            cnt+=1
    print(cnt)