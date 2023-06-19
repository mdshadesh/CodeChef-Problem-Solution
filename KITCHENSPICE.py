T = int(input())
for _ in range(T):
    X = int(input())
    if X < 4:
        category = "MILD"
    elif X < 7:
        category = "MEDIUM"
    else:
        category = "HOT"
    print(category)
