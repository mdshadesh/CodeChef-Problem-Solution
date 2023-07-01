import statistics

for _ in range(int(input())):
    num_o_numbers = int(input())
    thing = list(map(int, input().split()))
    
    mode = statistics.mode(thing)
    
    thing = list(filter(lambda a: a != mode, thing))
    
    print(len(thing))