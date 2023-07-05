T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    R = input()
    
    if S.count('1') == R.count('1') and S.count('0') == R.count('0'):
        print("YES")
    else:
        print("NO")
