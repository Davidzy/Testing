n = input()
cells = []
for i in xrange(n):
    cells.append(raw_input())
results = []
for i in cells:
    c = []
    for j in i:
        c.append(j)
    results.append(c)
        
for i in xrange(1, n-1):
    for j in xrange(1, n-1):
        if cells[i][j] > cells[i-1][j] and cells[i][j] > cells[i][j-1] \
           and cells[i][j] > cells[i+1][j] and cells[i][j] > cells[i][j+1]:
            results[i][j] = 'X'

for r in results:
    line = ''
    for j in r:
        line += j
    print line

