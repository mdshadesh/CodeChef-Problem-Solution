t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    buying_price = x - y
    new_selling_price = int(x * 1.1)
    new_profit = new_selling_price - buying_price
    print(new_profit)
