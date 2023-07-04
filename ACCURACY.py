# cook your dish here
t = int(input())

for i in range(t):
    x = int(input())
    
    if x%3 == 0:
        print(0)
        
    else:
        print(3-(x%3))
        