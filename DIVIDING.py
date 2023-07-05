N = int(input())
stamps = list(map(int, input().split()))

total_stamps = sum(stamps)
expected_sum = N * (N + 1) // 2

if total_stamps == expected_sum:
    print("YES")
else:
    print("NO")
