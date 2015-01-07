v = input()
n = input()
ar = [int(x) for x in raw_input().strip().split()]

for i in xrange(n):
    if ar[i] == v:
        print i
        break
