def solve(a, b, arr):
    total = sum(arr)
    if total >= a:
        return "No"
    else:
        return "Yes"

t = int(input())
for _ in range(t):
    input_data = input().split()
    a = int(input_data[0])
    b = int(input_data[1])
    arr = list(map(int, input_data[2:]))
    result = solve(a, b, arr)
    print(result)
