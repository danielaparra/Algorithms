#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  permutations = []
  options = ['rock', 'paper', 'scissors']

  def recurse_options(n, arr):
    if n == 0:
      return [[]] if arr == [] else arr
    else:
      if arr == []:
        for option in options:
          arr.append([option])
        return recurse_options(n - 1, arr)
      else:
        newArr = []
        for item in arr:
          for option in options:
            newItem = item.copy()
            newItem.append(option)
            newArr.append(newItem)
            print(newArr)
        return recurse_options(n - 1, newArr)

  permutations = recurse_options(n, [])

  #print(permutations)
  return permutations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')