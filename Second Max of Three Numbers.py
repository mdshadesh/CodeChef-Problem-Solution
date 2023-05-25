cses = int(input())
d=[]
for i in range(cses):
    a,b,c = map(int, input().split())
    l=[a,b,c]
    l.remove(max(l))
    d.append(max(l))
for i in d:
    print(i)
