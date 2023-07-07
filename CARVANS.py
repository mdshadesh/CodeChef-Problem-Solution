t = int(input())
for i in range(t):
    n = int(input())
    n_speed = list(map(int,input().split()))
    
    count=1
    max_speed = n_speed[0]
    for i in range(1,n):
        if n_speed[i]<= max_speed:
            count = count + 1
            max_speed = n_speed[i]
    print(count)