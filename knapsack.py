def nearest(ar, k):
    """return min difference from ar to k"""        
    ph, pt = 0, 0
    min_dif = k - min(ar)
    csum = [0 for i in xrange(2000)]
    for i in ar:
        if i not in csum:
            csum[pt] = i
            pt += 1

    while True:
        for i in ar:
            ai = i + csum[ph]
            if (ai not in csum) and ai <= k:
                csum[pt] = ai
                pt += 1
                min_dif = min(min_dif, k - ai)
        ph += 1    
        if ph == pt or min_dif == 0: break #if no new element was added, break the loop
    return k - min_dif       


        
T = input()
for i in xrange(T):
    n, k = [int(x) for x in raw_input().strip().split()]
    ar = [int(j) for j in raw_input().strip().split()]
    print nearest(ar, k)


            
        



    

