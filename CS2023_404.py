from sys import stdin,stdout
input = stdin.readline
from math import sqrt,gcd,ceil,inf,log2
from heapq import heapify,heappop,heappush


mod = 10**9 + 7
for _ in  range(int(input())):
    n = int(input())
    s = list(input().rstrip('\n'))   
    fz = 0
    f = 0
    ans = 0
    star = 0
    for i in s:
        if i == "*": 
            ans += ans%mod
            ans = ans%mod
            ans += fz%mod 
            ans = ans%mod
            fz += fz       
            fz += f%mod
            fz = fz%mod
            star += 1
            f *= 2
            f += int(pow(2,star-1,mod))
            f = f%mod
            
        elif i == '0':
            fz += f%mod
            fz = fz%mod
        else:
            ans += fz%mod
            ans = ans%mod
            f += int(pow(2,star,mod))
            f = f%mod
    print(ans%mod)        






