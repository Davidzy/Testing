#!/usr/bin/python

T = input()
def fib(n):
    rl = [0, 1]
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
        rl.append(b)
    return rl

fib_list = fib(10**10)
isfib = 'IsFibo'
notfib = 'IsNotFibo'
for i in range(T):
    a = input()
    if a in fib_list:
        print isfib
    else: print notfib

