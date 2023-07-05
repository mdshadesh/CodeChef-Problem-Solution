T = int(input())

for tc in range(T):
    N = int(input())
    sq = 0
    while N >= 1:
        sr = int(N ** 0.5)
        sq += 1
        N -= sr ** 2
    print(sq)
