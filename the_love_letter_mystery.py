T = input()
def op_times(s):
    cnt = 0
    l = len(s) / 2 - 1
    r = len(s) - l - 1
    while l >= 0:
        cnt += abs(ord(s[l])-ord(s[r]))
        l -= 1
        r += 1
    return cnt
    
for i in xrange(T):
    s = raw_input()
    print op_times(s)
