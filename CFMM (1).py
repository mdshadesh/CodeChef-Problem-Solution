x = int(input())

for _ in range(x):
    l = []
    a = int(input())
    
    for _ in range(a):
        ele = input()
        l.append(ele)
    
    l = ''.join(l)
    c = l.count('c')
    o = l.count('o')
    d = l.count('d')
    e = l.count('e')
    h = l.count('h')
    f = l.count('f')
    
    p = min(c // 2, o, d, e // 2, h, f)
    print(p)
