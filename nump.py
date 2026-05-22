import numpy as np
'''
array = np.array([1,2,3,4,5])
array = array * 2
print(array)
print(type(array))

array = np.array('A')
print(array.ndim)
# u can change the dim by adding a matrix formation, more than one list will give 2D whereas nested list will give 3D

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
#array[start:stop:step] just like loop
print(array[1:4])
print(array - 1)#arithmetic
print(array *100)
'''

#vectorized math funcs
array = np.array([1,2,3])
print(np.sqrt(array))


print(f"Pi to 2 decimal places: {np.pi:.2f}")#works only when you use f{}
print(np.round(np.pi,2)) #another way

