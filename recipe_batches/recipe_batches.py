#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipeKeys = recipe.keys()
  ingredientKeys = ingredients.keys()

  if not all(elem in ingredientKeys for elem in recipeKeys):
    return 0
  else:
    numBatches = []
    for key in recipeKeys:
      recipeAmount = recipe[key]
      if recipeAmount > ingredients[key]:
        return 0
      else:
        numBatches.append(ingredients[key] // recipeAmount)
    
    return min(numBatches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))