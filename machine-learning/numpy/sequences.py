'''creating sequences of numbers in numpy so
# we can use function arange()  ,,it returs numpy array'''
# arange()
# arange(start,stop,step)

import numpy as np
arr=np.arange(1,100,5)
print(arr)

#to calculate  and creating identity matrix in numpy\
#function= eye(size)

identity_matrix=np.eye(4)
print(identity_matrix)