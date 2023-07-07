import sys
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum1=sys.maxsize
    sum2=sum(a)
    for i in range(n):
        sum2+=a[i]
        if(sum2<sum1):
            sum1=sum2
            index=i
        sum2-=a[i]
    print(index+1)