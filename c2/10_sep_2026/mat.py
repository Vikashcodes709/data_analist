# to print a numpy contain zeros vector
'''import numpy as np
v=np.zeros(12)
print(v)'''

'''v[5]=1
print(v)'''

#create a vector with values ranging from 10 to 100
'''b=np.arange(10,100)
print(b)'''

#2D array
'''b=np.arange(10,19).reshape(3,3)
print(b)'''

#to generate identity matrix
'''a=np.eye(3)
print(a)'''

#create to random matrix of 3*3*3
'''d=np.random.random((3,3,3))
print(d)'''

#to create a 5*5 array with random value and find the maxi and mini values.
'''d=np.random.random((5,5))
dmin,dmax=d.min(),d.max()
print(dmin,dmax)'''

#questions *****
#1.create an array of 20 zeros 
#2.create an array of 15 ones
#3.create array of 10 fives 
#4.create an array of all even integers from 5 to 90
'''zeros = [0] * 20
print(zeros)

ones = [1] * 15
print(ones)

fives = [5] * 10
print(fives)

even_numbers = list(range(6, 91, 2))
print(even_numbers)'''


#Questions_2
#create a 7*7 identity matrix
#generate a number of an array of 30 random sample from a standard normal dist.
#range to random (0 to 1).
'''import numpy as np

# 1. Create a 7 × 7 identity matrix
identity_matrix = np.eye(7)
print("7 × 7 Identity Matrix:")
print(identity_matrix)

# 2. Generate an array of 30 random samples
#    from a standard normal distribution (mean = 0, std = 1)
normal_array = np.random.randn(30)
print("\n30 Random Samples from Standard Normal Distribution:")
print(normal_array)

# 3. Generate random numbers in the range 0 to 1
random_array = np.random.rand(30)
print("\n30 Random Numbers between 0 and 1:")
print(random_array)'''


#Questions.
#create an array suing and perform slicing.

# Create an array
arr = [10, 20, 30, 40, 50, 60, 70]

# Slicing examples
print("Original array:", arr)
print("First 3 elements:", arr[:3])
print("Elements from index 2 to 5:", arr[2:6])
print("Last 3 elements:", arr[-3:])
print("Every second element:", arr[::2])
print("Reversed array:", arr[::-1])


