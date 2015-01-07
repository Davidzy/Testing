from math import sqrt
T = int(raw_input())
for i in xrange(T):
    a, b = [int(x) for x in raw_input().strip().split()]
    sa = sqrt(a)
    sb = sqrt(b)
    if int(sa) == sa:
        print int(sb) - int(sa) + 1
    else:
        print int(sb) - int(sa)

