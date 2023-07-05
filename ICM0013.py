# cook your dish here
for _ in range(int(input())):
    n = int(input())
    count = 0
    m = 1
    while m <= n:
        if (n % m) <= (n // 2):
            count += 1
        m += 1
    print(count)
