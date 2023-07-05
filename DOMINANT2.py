from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=Counter(l)
    ll=[i for i in c.values()]
    m=max(ll)
    if(ll.count(m)==1):
        print("YES")
    else:
        print("NO")
    