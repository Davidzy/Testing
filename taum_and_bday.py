T = input()

def totalcost(B, W, bc, wc, z):
    # if black is cheaper than white - z ( bc < wc - z)
    # then buy black and convert them to white
    cost = 0
    if bc < wc - z:
        wc = bc + z    
    # else if white is cheaper than black - z (wc < bc - z)
    # then buy white and convert them to black
    elif wc < bc - z:
        bc = wc + z   
    # else |black - white| < z
    # then buy B black and W white 
    cost = bc * B + wc * W
    return cost

for i in xrange(T): 
    B, W = [int(x) for x in raw_input().strip().split()]
    bc, wc, z = [int(x) for x in raw_input().strip().split()]    
    mincost = totalcost(B, W, bc, wc, z)
    print mincost
