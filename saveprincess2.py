def nextMove(n,r,c,grid):
    #locate the princess
    for i in xrange(n):
        if 'p' in grid[i]:
            rp = i
            break
    for i in xrange(n):
        if 'p' == grid[rp][i]:
            cp = i
            break
    if rp < r:
        direction = "UP"
    elif rp > r:
        direction = "DOWN"
    elif cp < c:
        direction = "LEFT"
    elif cp > c:
        direction = "RIGHT"
    return direction
    
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
