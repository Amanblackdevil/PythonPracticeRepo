from numpy import random
x = random.randint(100)
print(x)

#generate random float
randomFloat = random.rand()
print("Random float number :", randomFloat)

#Generate number array
randomArray = random.randint(100, size=5)
print(randomArray)

#Generate 2-D array
random2Darray = random.randint(100, size=(5, 3))
print("2-D array")
print(random2Darray)

#Generate random number from an array with the help of choice

randomNumberFromArray = random.choice([3, 10, 90, 100])
randomNumberFromArraywithSize = random.choice([3, 5, 7, 9], size=(3, 5))
print("Random Number from an Array :", randomNumberFromArray)
print("Random number from an array with the help of size :")
print(randomNumberFromArraywithSize)

