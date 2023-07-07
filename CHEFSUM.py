import math as m
def input1():
    return int(input())
def input2():
    return str(input())
def input3():
    return map(int,input().strip().split())
def input4():
    return list(map(int,input().strip().split()))

def solve():
    n=input1()
    a=input4()
    idx=0
    mini = a[0]
    for i in range(1,n):
        if mini>a[i]:
            mini = a[i]
            idx = i
    print(idx+1)
        