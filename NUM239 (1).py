t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    
    count = 0
    for num in range(l, r+1):
        last_digit = num % 10
        if last_digit == 2 or last_digit == 3 or last_digit == 9:
            count += 1
    
    print(count)
