n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()

def mindiff(N, K, x):
    minx = x[-1] - x[0]
    p1 = 0
    while p1 <= N - K:
        minb = x[p1 + K - 1] - x[p1]
        minx = (minb if minb < minx else minx)
        #change p1
        p1 += 1
    return minx
min_diff = mindiff(n, k, candies)    
print min_diff
