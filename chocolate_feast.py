T = int(raw_input())
def eat_num(n, c, m):
    tot = 0
    tot = n / c
    reminder = n / c
    while reminder >= m:
        new = reminder / m
        tot += new
        reminder = reminder % m
        reminder += new 
    return tot
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]    
    answer = eat_num(A, B, C1)
    # write code to compute answer
    print answer
