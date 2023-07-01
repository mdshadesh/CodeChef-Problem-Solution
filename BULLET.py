t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())

    # Calculate the time it takes for the bullet to reach the goomba
    time = y // x

    # Adjust the time if needed
    if time < z:
        time = z

    print(time)
