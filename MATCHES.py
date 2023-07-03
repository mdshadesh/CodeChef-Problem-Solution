
t = int(input())

matches = [6,2,5,5,4,5,6,3,7,6]

for _ in range(t) :
    a,b = map(int, input().split(" "))
    num = 0
    ab = a+b 
    while(ab):
        x = int(ab%10)
        ab = int(ab/10)
        num = num + matches[x]
    print(num)