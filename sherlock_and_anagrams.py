import time
# divide the string to all its substring
def generate_substring(st):
    subset = []
    for startp in xrange(len(st)):
        for endp in xrange(startp+1, len(st)+1):
            substr = st[startp:endp]
            subset.append(substr)
    return subset

# judge whether two substring is anagram
def count_char(st):
    d = {}
    for c in st:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d
def dict_substring(alist):
    d = {}
    for ele in alist:
        if ele not in d:
            d[ele] = count_char(ele)
    return d
    
def is_anagram(str1, str2, d):
    if len(str1) != len(str2):
        return False
    d1 = d[str1]
    d2 = d[str2]
    for i in xrange(len(str1)):
        if d1[i]
    return True

def count_anagram(slist, d):
    cnt = 0
    pt = 0
    while pt < len(slist) - 1:
        for comp in xrange(pt + 1, len(slist)):
            # find different
            # compare slist[pt] slist[comp]
            if len(slist[comp]) != len(slist[pt]):
                continue
            if is_anagram(slist[pt], slist[comp], d):
                cnt += 1
        # in the while loop
        #print 'time', time2 - time1
        pt += 1        
    return cnt
    
def count_anagram2(slist, d):
    cnt = 0
    backet = {} # contain all different strings
    for ele in slist:
        if ele in backet:
            backet[ele] += 1
        else:
            backet[ele] = 1
    hascounted = []
    for kh in backet:
        hascounted.append(kh)
        cnt += backet[kh] * (backet[kh] - 1) / 2
        for kt in backet:
            if kt in hascounted:
                continue
            if len(kh) != len(kt):
                continue
            if is_anagram(kh, kt, d):
                cnt += backet[kh] * backet[kt]
    return cnt

# main
T = input()
for i in xrange(T):
    time1 = time.time()
    inputstr = raw_input()
    strlist = generate_substring(inputstr)
    d = dict_substring(strlist)
    print len(d)
    ans = count_anagram2(strlist, d) 
    print ans
    time2 = time.time()
    print time2 - time1

