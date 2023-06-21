n = int(input())
for i in range(n):
    if (int(input()))==1:
        a=list(map(int,input().split()))
        del a 
        print(1)
        continue
    print(int(not(sum(list(map(int,input().split())))%2==0))+1)