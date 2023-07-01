n = int(input())
scores = []

for _ in range(n):
    s, t = map(int, input().split())
    scores.append((s, t))

max_lead = 0
winner = 0

cumulative_s1 = 0
cumulative_s2 = 0

for s, t in scores:
    cumulative_s1 += s
    cumulative_s2 += t
    
    lead = abs(cumulative_s1 - cumulative_s2)
    
    if lead > max_lead:
        max_lead = lead
        
        if cumulative_s1 > cumulative_s2:
            winner = 1
        else:
            winner = 2

print(winner, max_lead)
