T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    if (N/M)%2==0:
        print("yes")
    else:
        print("no")