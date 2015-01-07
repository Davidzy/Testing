n, m = [int(i) for i in raw_input().strip().split()]
s = []
for i in xrange(n):
    ss = raw_input()
    s.append(ss)
# input done

def longest_topic(s1, s2):
    l = 0
    for i in xrange(len(s1)):
        if s1[i] != '0' or s2[i] != '0':
            l += 1
    return l
# d save all kinds of l

def most_team(s):
    d = {}
    for i in xrange(n-1):
        for j in xrange(i+1,n):
            l = longest_topic(s[i], s[j])
            if l in d:
                d[l] += 1
            else: d[l] = 1
    a = sorted(d)
    return a[-1], d[a[-1]]

        
topic, teams = most_team(s)
print topic
print teams

