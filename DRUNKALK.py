for t in range(int(input())):
    c = 0
    for i in range(int(input())):
        if i%2 == 0:
            c+=3
        else:
            c-=1
    print(c)