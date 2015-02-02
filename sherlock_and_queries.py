N, M = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]
b = [int(x) for x in raw_input().split()]
c = [int(x) for x in raw_input().split()]

matrix = [ [] for x in xrange(N)]
print 'done'

for i in xrange(M):
    for j in xrange(N):
        if (j + 1) % b[i] == 0:
            matrix[j].append(c[i])

root = 10 ** 9 + 7

for i in xrange(N):
    for j in matrix[i]:
        a[i] *= j
        if a[i] > root: 
            a[i] = a[i] * j % root
    
for ele in a:
    print ele,
