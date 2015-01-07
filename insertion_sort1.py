def insertionSort(ar):    
    v = ar[-1]
    pt = -2
    
    while ar[pt] > v:
        ar[pt + 1] = ar[pt]
        for e in ar:
            print e,
        print
        pt -= 1
        if pt * -1 == len(ar): break
    if ar[pt] > v:
        ar[pt+1] = ar[pt]
        for e in ar:
            print e,
        print
        ar[pt] = v
        for e in ar:
            print e,
        print    
    else:
        ar[pt + 1] = v
        for e in ar:
            print e,
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
