import sys

def deal(keyword):
    firstrow = []
    for c in keyword:
        if c not in firstrow:
            firstrow.append(c)
    return firstrow
        
def cipher_list(keyword):
    #list
    firstrow = deal(keyword)
    # finish firstrow SECRT
    clist = [i for i in firstrow]
    Aint = ord('A')
    r = 1
    for i in xrange(26):
        c = chr(Aint + i)
        if c not in firstrow:
            clist.append(c);
    # transform
    return clist     
def off_set(origin, sortkw):
    d1 = {origin[i] : i for i in xrange(len(origin))}
    offset = [d1[key] for key in sortkw]
    return offset

def cipher_transform(keyword, alist):
    newlist = []
    kw = deal(keyword)
    skw = sorted(kw)
    offset = off_set(kw, skw)
    for i in offset:
        pt = i
        while pt < 26:
            newlist.append(alist[pt])
            # print offset[i], pt + offset[i], alist[pt]
            pt += len(kw)
    d = {newlist[i]: chr(ord('A') + i) for i in xrange(26)} 
    return d
        
T = input()
for i in xrange(T):
    keyword = raw_input().strip()
    code = raw_input().strip()
    d = cipher_transform(keyword, cipher_list(keyword))
    d[' '] = ' '
    for c in code:
        sys.stdout.write(d[c])
    print
