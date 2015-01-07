n, m = [int(i) for i in raw_input().strip().split()]
tot = 0
for i in xrange(m):
    a, b, q = [int(i) for i in raw_input().strip().split()]
    tot += (b - a + 1) * q
print int(tot / n)
