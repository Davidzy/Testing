def ans(n):
    """return a string
    -1 means no such number
    most 5 and then 3"""
    n5, n3 = 0, 0
    for n3 in xrange(int(n/5) + 1):
        if (n - 5 * n3) % 3 == 0:
            n5 = (n - 5 * n3) / 3
            break
    s = '5' * n5 * 3 + '3' * n3 * 5
    if len(s) == n:
        return s
    else: 
        return '-1'
    
T = input()
for i in xrange(T):
    num = input()
    print ans(num)

