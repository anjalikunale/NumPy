#Q: check wether a list is empty or not
#explicit way
list0=[0]
list1=[0,1]
list2=[]
lists=[list0,list1,list2]
def enquiry(list_n):
	if len(list_n)==0:
		return 1
	else:
		return 0

for lis in lists:
	if enquiry(lis):
		print(f"{lis} list is empty")
	else:
		print(f"{lis} list is not empty")
		
print(not list0)
print(not list1)
print(not list2)

#implicit way / pythonic way

def Enquiry(list_n):
	if not list_n:
		return 1
	else:
		return 0

for lis in lists:
	if Enquiry(lis):
		print(f"{lis} list is empty")
	else:
		print(f"{lis} list is not empty")
		
#numpythonic way
import numpy
def enquire(list_n):
	return (numpy.array(list_n))

for lis in lists:
	if enquire(lis).size:
		print(f"{lis} list is not empty")
	else:
		print(f"{lis} list is empty")

print("~~~"*5,"qestion2","~~~"*5)		
#Q: Create a list with unique values from existing list
	
list5=[10,20,10,10,30,40,40,30]

#method 1: explicit way
#create empty list
unique_list=[]  
def unique(my_list):
	for x in list5:
		if x not in unique_list:
			unique_list.append(x)
	print(unique_list)

unique(list5)

#method 2: using set and list typecast

def unique(mylist):
	#convert in set
	set_list=set(mylist)
	unique_list=list(set_list)
	return unique_list

print(unique(list5))

#method 3: numpy.unique(list_name)

import numpy as np
def unique(my_list):
	#convert in array
	x=np.array(my_list)
	return (np.unique(x))

print(unique(list5))

print("~~~"*5,"qestion3","~~~"*5)

#print the product of all elements from given list
list6=[1,2,3,4,5]
#method1: using traversal

def product(my_list):
	product=1
	for num in my_list:
		product=product*num
	return product

print(product(list6))

#method2: using math.prod()

import math

result=(math.prod(list6))
print(result)

#method3: using numpy.prod()

import numpy as np

result=np.prod(list6)
print(result)

#method4: using reduce method 

from functools import reduce

result=reduce(lambda x,y: x*y, list6)
print(result)

