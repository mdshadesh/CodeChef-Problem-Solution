T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    if X < Y:
        print("FIRST")
    elif X > Y:
        print("SECOND")
    else:
        print("ANY")
