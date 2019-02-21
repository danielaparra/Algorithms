#!/usr/bin/python

import sys

options = ['rock', 'paper', 'scissors']

def recurse(n, arr, option):
  
  newArr = arr
  if n == 0:
    newArr = [[]] if arr == [] else arr
  else:
    if newArr == []:
      newArr.append([option])
      return recurse(n-1, arr, option)
    else:
      print(arr)
      print(n)
      for item in arr:
        for option in options:
          newItem = item
          newItem.append(option)
          newArr.append(newItem)
          print(newItem)
        newArr.remove(item)
      return recurse(n-1, newArr, option)
    
    #check for repeats
  print(newArr)
  return newArr

def rock_paper_scissors(n):
  permutations = []
  options = ['rock', 'paper', 'scissors']

  

  for option in options:
    permutation_for_option = recurse(n,[],option)
    permutations.append(*permutation_for_option)

  print(permutations)
  return permutations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')