N, T = [int(x) for x in raw_input().split()]
width = [int(x) for x in raw_input().split()]
if len(width) != N:
    print 'input error'
    
for i in xrange(T):
    entry, exit = [int(x) for x in raw_input().split()]
    v = 3
    for j in xrange(entry, exit+1):
        if width[j] == 1:
            v = 1
            break
        if v > width[j] and width[j] == 2:
            v = 2
    print v
