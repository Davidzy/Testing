def judge(n, a):
    s = sum(a)
    ls = a[0]
    flag = False
    for i in xrange(1, n):
        if ls * 2 == s - a[i]:
            flag = True
        ls += a[i]
    if len(a) == 1:
        flag = True
    if flag:
        return "YES"
    else:
        return "NO"


T = input()
for i in xrange(T):
    n = input()
    a = [int(i) for i in raw_input().strip().split()]
    print(judge(n,a))
