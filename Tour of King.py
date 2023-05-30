# cook your dish here


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    max_people = (n * 5) + (m * 7)
    print(max_people)
