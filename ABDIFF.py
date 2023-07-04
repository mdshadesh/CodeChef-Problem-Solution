A, B = map(int, input().split())

correct_answer = A + B
chef_output = A * B

difference = abs(correct_answer - chef_output)

print(difference)
