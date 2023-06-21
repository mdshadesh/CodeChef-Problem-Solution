x, y, h = map(int, input().split())

if h == 1:
    total_charges = x
else:
    total_charges = x + (y * (h - 1))

print(total_charges)
