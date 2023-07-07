for _ in range(int(input())):
    n=int(input())
    m= list(map(int,input().split()))
    a=m[0]
    for i in range(n-1):
        if m[i]<=m[i+1]:
            a+= m[i+1]-m[i]
    print(a)