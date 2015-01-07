T = input()
for i in xrange(T):
    n = input()
    a = input()
    b = input()
    ab = a + b
    a = ((ab - a) if a > b else ab - b)
    b = ab - a
    result = []
    for c in xrange(n-1, -1, -1):
        r = c * a + (n-1 - c) * b
        if not r in result:
            result.append(r)
    for x in result:
        print x, 
    print
