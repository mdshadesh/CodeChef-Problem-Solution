T = int(input())

for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # Check if any of the numbers is even
    if any(num % 2 == 0 for num in numbers):
        print("NO")
    else:
        print("YES")
