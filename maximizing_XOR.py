

def maxXor(l,  r):
  max_xor = 0
  for i in xrange(l, r + 1):
      for j in xrange(l, r + 1):
          cur_xor = i ^ j
          max_xor = (cur_xor if cur_xor > max_xor else max_xor)
  return max_xor
          
      

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
