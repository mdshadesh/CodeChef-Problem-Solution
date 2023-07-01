t = int(input())

for _ in range(t):
    x = int(input())
    size = "NORMAL"  # Mario's initial size is normal

    # Determine Mario's size after eating x mushrooms
    for _ in range(x):
        if size == "NORMAL":
            size = "HUGE"
        elif size == "HUGE":
            size = "SMALL"
        else:
            size = "NORMAL"

    print(size)
