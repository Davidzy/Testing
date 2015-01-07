n = input()
a = [int(i) for i in raw_input().strip().split()]

while len(a) > 0:
    a.sort()
    while len(a) > 0 and a[0] == 0:
        a.pop(0)
    if len(a) > 0:
        print len(a)
    for i in xrange(1, len(a)):
        a[i] -= a[0]
    if len(a) > 0:
        a[0] = 0
        
