def calculate_notes(N):
    total_amount = N * 2000
    notes_500 = total_amount // 500
    if total_amount % 500 != 0:
        notes_500 += 1
    return notes_500

N = int(input())

result = calculate_notes(N)

print(result)
