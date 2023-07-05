t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count_0 = s.count('0')
    count_1 = s.count('1')
    if count_0 != count_1:
        print(min(count_0, count_1) * 2 + 1)
    else:
        print(min(count_0, count_1) * 2)
