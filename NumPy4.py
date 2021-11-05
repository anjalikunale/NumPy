
		#Mathematics operations in numpy
import numpy as np

a=np.array([1,2,3,4])
print(a)

print(a+2)

print(a-2)

print(a*2)

print(a/2)

b=np.array([1,0,1,0])

print(a+b)

print(a*b)

print(a**2)

		#take the sin and cos 
print(np.sin(a))
print(np.cos(a))

		##Linear Algebra
		#we cant multipy two matrices if their shape is different but we can multiply it in numpy using matmul function

x=np.ones((2,3))
print(x)
y=np.full((3,2),2)
print(y)
print(np.matmul(x,y))

		#find determinant of matrix
z=np.identity(4)
print((np.linalg.det(z)))

		##Statistics

stats=np.array([[1,2,3,4],[5,6,7,8]])
print(stats)

print(np.min(stats))
print(np.max(stats))

print(np.sum(stats))

		##Recognizing Arrays

before=np.array([[1,2,3,4],[5,6,7,8]])
print(before)

print(before.reshape(4,2))
print(before.reshape(8,1))
after=before.reshape((2,2,2))
print(after)

		###Stacking
		#1. Vertically stacking : repeat vectors vertically

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

print(np.vstack([v1,v2]))
print(np.vstack([v1,v1,v2,v2,v1]))
print(np.vstack([v1,v1]))

		#2. Horizontal stacking : repeat vectors horizontally 

h1=np.ones((2,4))
h2=np.zeros((2,2))

result1=(np.hstack([h1,h2]))
result2=np.hstack([h1,h2,h1])

print(result1)
print(result2)

		##Miscellaneous
		#Load data from file

print(np.genfromtxt("NumPy4.txt",delimiter=","))

filedata=np.genfromtxt("NumPy4.txt",delimiter=",")
filedata=filedata.astype("int32")
print(filedata)