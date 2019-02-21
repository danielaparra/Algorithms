#!/usr/bin/python

import sys

def climbing_stairs(n, cache=None):
  c = [0] * (n+1) if cache is None else cache
  
  if len(c) >= n + 1 and c[n] > 0:
    return c[n]
  elif n == 0:
    c[n] = 1 
    return 1
  elif n in [1, 2]:
    c[n] = n
    return n
  else:
    result = climbing_stairs(n-1, c) + climbing_stairs(n-2, c) + climbing_stairs(n-3, c)
    c.insert(n, result)
    return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')