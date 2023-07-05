for _ in range(int(input())):
    n, k = map(int, input().split())
    distances = list(map(int, input().split()))
    result = ""
    for d in distances:
        if d % k == 0:
            result += "1"
        else:
            result += "0"
    print(result)
