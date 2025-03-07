import numpy as np 

#we are learning how to create arrays in numpy 
array = np.array([1,2,3,4,5])

array2d = np.array([[1,2,3,4], [5,6,7,8]])


#creating matrices with 0's and 1's 
arrZeroes = np.zeros((4,5))
arrOnes = np.ones((2,5))

print(array)
print(array2d)

#the "shape" method tells the number of rows and columns in an array 
print(array.shape)
print(array2d.shape)


#printing 0's and 1's matrices 
print(arrZeroes)
print(arrOnes)