import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, False, True]
newarray = arr[x]
print(newarray)

#Based on condition
#WAP where a array should contain if the number is greater than 40
array1 = np.array([55, 41, 39, 40, 24, 66, 10, 90])
filter_array = []

for element in arr:
    if element > 40:
        filter_array.append(True)
    else:
        filter_array.append(False)


newarray1 = arr[filter_array]
print("Filter Array :", filter_array)
print("Printing new array where we have stored filtered array :", newarray1)

#Creating filter directly from array
directlyFromArray = np.array([41, 42, 43, 44])
filter_array_directlyFromArray = directlyFromArray > 42
newArrayDirectlyFromArray = directlyFromArray[filter_array_directlyFromArray]
print("Printing filtered array directrly :", filter_array_directlyFromArray)
print("Printng filtered array after storing it into some other array:", newArrayDirectlyFromArray)