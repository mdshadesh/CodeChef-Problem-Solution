# Read the threshold limit and Chef's current brain speed
X, Y = map(int, input().split())

# Check if Chef is prone to errors
if Y > X:
    print("YES")
else:
    print("NO")
