#! /usr/bin/python
def displayPathtoPrincess(n, grid):
    #Locate whether p is on the top corner
    distance = n / 2
    if 'p' in grid[0]:
        for i in xrange(distance):
            print 'UP\n',
        pat = grid[0]
    else: 
        for i in xrange(distance):
            print 'DOWN\n',
        pat = grid[-1]
    #Locate whether p is on the left corner
    if 'p' in pat[0]:
        for i in xrange(distance):
            print 'LEFT'
    else: 
        for i in xrange(distance):
            print 'RIGHT'
    
    
#print all the moves here
m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
