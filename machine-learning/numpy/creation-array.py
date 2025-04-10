#  creating arry from python lists
#function>np.array([])
# with default values
# numpy provides an bulit in function which is function> np.zeros(shape of an arry) shape=size of an aray ex=(3)for 1D, (3,3)for 2D,

import numpy as np
# for 1D
zeroes_array=np.zeros(3)
print(zeroes_array)


# ones(shape)
ones_array=np.ones((3,3))
print(ones_array)


#if i want fill different  array value so 
# function> full(shape,value)
filled_array=np.full((2,2),7) ,#defalut shape=2,2 value = 7
print(filled_array)


