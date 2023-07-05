from collections import Counter

n1, n2, n3 = map(int, input().split())

list1 = [int(input()) for _ in range(n1)]
list2 = [int(input()) for _ in range(n2)]
list3 = [int(input()) for _ in range(n3)]

combined_list = list1 + list2 + list3

counts = Counter(combined_list)

final_list = [num for num, count in counts.items() if count >= 2]

final_list.sort()

print(len(final_list))
for num in final_list:
    print(num)
