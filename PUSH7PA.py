for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    if n == 1:
        print(h[0])
    else:
        for j in set(h):
            c=h.count(j)
            if j+c-1 > max:
                max = j+c-1
        print(max)