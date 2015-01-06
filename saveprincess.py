#! /usr/bin/python
def displayPathtoPrincess(n, grid):
    #Locate whether p is on the top corner
    if 'p' in grid[0]:
        print 'UP\n',
        pat = grid[0]
    else: 
        print 'DOWN\n',
        pat = grid[-1]
    #Locate whether p is on the left corner
    if 'p' in pat[0]:
        print 'LEFT'
    else: print 'RIGHT'
    
    
#print all the moves here
m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
