import numpy as np
#all zeros matrix •Symtax: numpy.zeros(shape)
z1=np.zeros(3,dtype="int32")
print(z1)

z2=np.zeros((2,3))
print(z2)

z3=np.zeros((3,2,3))
print(z3)

#all ones matrix •syntax: numpy.ones(shape)
o1=np.ones(3)
print(o1)

o2=np.ones((3,3))
print(o2)

o3=np.ones((3,2,3))
print(o3)

#any other number •syntax: numpy.full(shape,number)

n1=np.full(3,99)
print(n1)

n2=np.full((3,4),4)
print(n2)

n3=np.full((3,2),5)
print(n3)

print("~~~"*5,"Exercuse","~~~"*5)
''' 
create this matrix
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1
'''

o=np.ones((5,5),dtype="int32")
print(o)

z=np.zeros((3,3),dtype="int32")
z[1,1]=9
print(z)

o[1:4,1:4]=z
print(o)

#any other number like syntax: numpy.full_like(array_name,numver)
a=np.array([[1,2,3,4],[5,6,7,8]])
f1=np.full_like(a,7) # it will copy the shape of array "a"
print(f1)

#without using full_like
f2=np.full(a.shape,9)
print(f2)

#Random decimal number
r1=np.random.rand(3,2)
print(r1)

#Random integer value
r2=np.random.randint(9,size=5)
print(r2)

r3=np.random.randint(5,9,size=5)
print(r3)

#identity matrix
#•identity function take only one argument.
#•in identity matrix row number and column number is same

i1=np.identity(4)
print(i1)

i2=np.identity(4,dtype="int32")
print(i2)

#Repeat matrix
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.repeat(b,2) #it will repeat elements
d=np.repeat(b,2,axis=0) #it will repeat rows
print(c)
print(d)


