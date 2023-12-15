from numpy import random
x = random.choice([3, 5, 7, 8], p=[0.1, 0.3, 0.6, 0], size=(100))
print(x)
random2Darray = random.choice([3, 5, 6, 7], p=[0.1, 0.4, 0.5, 0], size=(3, 5))
print("Random 2-D Array:")
print(random2Darray)