
t = int(input())

for _ in range(t):
  x, y = map(int, input().split())
  schedule = input()

  count_1 = 0
  count_streak=0
  max_streak = 0

  for i in range(len(schedule)):
    if schedule[i] == '1':
      count_1 += 1
      count_streak += 1
      max_streak = max(count_streak,max_streak)
    else:
      count_streak = 0
  
  print(x*count_1 + y*max_streak)