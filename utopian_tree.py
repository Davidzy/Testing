T = input()
def tl(cycles):
    hlist = [1]
    h = 1
    for i in xrange(cycles / 2 + 1):
        h *= 2
        hlist.append(h)
        h += 1
        hlist.append(h)
    return hlist

l = tl(60)
        
for i in xrange(T):
    n = input()
    print l[n]
