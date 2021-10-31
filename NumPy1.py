'''
•Applications of NumPy
1.Mathematics
2.Backend(pandas,connect4)
3.Plotting(Matplotlib)
4.Machine Learning

'''
#import numpy module
import numpy as np

#array of rank 1 i.e 1D array
a=np.array([1,2,3,4])
print(f"1d array,\n {a}")

#data type of array
print(a.dtype)

#size of each item
print(a.itemsize)

#size of array
print(a.size)

#total size
print(a.size*a.itemsize)

# dimension of array : one-d array
print(a.ndim)

#shape of array i.e (row count,column count)
print(a.shape)

#accesing array elements [row-i,clm-i]
print(a[3])

#•2D array
b=np.array([[1,2,3,4,5,6,7],[5,6,7,8,9,10,11]], dtype="int32")

print(f"2d array, \n {b}")

print(f"shape of array {b.shape}")

print(f"dimension {b.ndim}")

print(f"total size {b.nbytes}")

#•accessing,changing specific elements,row,column,etc

#get specific element name[r-ind,c-ind]
print(f"specific ele {b[1,1]}")
print(f"specific ele {b[0,2]}")

#get specific row name[r-ind, :]
print(f"specific row {b[1,:]}")

#get specific column name(: ,c-ind)
print(f"specific colm {b[:,2]}")

#getting little more fancy [start_index : end_index : step_size]

print(b[1,1:6:2]) # 1st row from 1st ele till 6th ele skiping 1 ele

#change specific element
b[0,3]=100
print(b)

#change whole column
b[:,6]=0
print(f"changed whole column \n{b}")

#change whole row
b[0,:]=5
print(f"changed whole row \n{b}")

#change specific slice
b[0,2:5]=0
print(f"changed small slice \n{b}")

#•3d array
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

print(f"access specific element {c[0,1,1]}")
print(f"access specific col {c[:,:,1]}")
print(f"access specific row {c[1,0]}")
print(f"access specific {c[:,:,:]}")