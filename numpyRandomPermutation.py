#Shuffle
from numpy import random
import numpy as np
shuffleArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
random.shuffle(shuffleArray)
print("Shuffler Array:", shuffleArray)

#Permutation
permutationArray = np.array([1, 2, 3, 4, 5, 6])
print("Permutation Array :", random.permutation(permutationArray))
print(permutationArray.base)
