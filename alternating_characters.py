T = input()
def del_num(s):
    cnt = 0
    p1=0
    for i in xrange(1, len(s)):
        if s[p1] != s[i]:
            p1 = i
        else: cnt += 1
    return cnt
    
for i in xrange(T):
    s = raw_input()
    print(del_num(s))
