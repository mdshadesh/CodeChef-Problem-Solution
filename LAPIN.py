from collections import Counter

for _ in range(int(input())):
    s = input().strip()
    l = Counter(s[:len(s)//2])
    if len(s)%2:
        r = Counter(s[len(s)//2+1:])
    else:
        r = Counter(s[len(s)//2:])
    print('YES' if l==r else 'NO')