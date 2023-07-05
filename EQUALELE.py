from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    max_count = max(counter.values())
    print(n - max_count)
