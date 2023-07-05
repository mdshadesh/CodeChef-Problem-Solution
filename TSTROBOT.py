
def robot(n,x):
    string = list(input())
    new = [x]
    for i in string:
        if i == "R":
            new.append(new[-1] + 1)
        else:
            new.append(new[-1] - 1)
    return (len(set(new)))
   
m=int(input())
for i in range(m):
    n,x=map(int,input().split())
    print(robot(n,x))



