t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    diff = abs(x - y)
    presses = diff // 2 + diff % 2
    
    print(presses)
