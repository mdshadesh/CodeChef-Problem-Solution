t = int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if(m>=n+k):
        print("YES")
    else:
        print("No")