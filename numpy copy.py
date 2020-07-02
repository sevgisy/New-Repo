#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:02:08 2020

@author: sevgisaracyilmaz
"""

import numpy as np

array = np.array([1,2,3,4])
 
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print([array.shape])

a = array.reshape(3,5)

print("dimension:", a.ndim)

print("data type:", array.dtype.name)

print("size:", a.size)


array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

array1.shape

zeros = np.zeros((3,4))

zeros[0,0] = 5

ones = np.ones((3,4))

np.empty((2,4))

np.arange(10,50,5)

a = np.linspace(10,50,20)
a

np.zeros((2,1))

# %%
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))
print(a<2)

a =np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print(a*b)
print(a.dot(b))
print(a.dot(b.T))
print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis = 0))
print(a.sum(axis = 1))
print(np.sqrt(a))
print(np.square(a))
print(a**2)
print(np.add(a,a))
print(a+a)
# %%
# indexing and slicing

array = np.array([1,2,3,4,5,6,7])

print(array[0])
print(array[3])
print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])
print(array1[:,1])
print(array1[1,1:4])
print(array1[-1,:])
print(array1[:,-1])
# %%
# shape manuplation


array = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = array.ravel()
print(a)

array2 = a.reshape(3,3)

arrayT = array2.T
print(arrayT.shape)
print(arrayT)

array5 = np.array([[1,2],[3,4],[4,5]])
array5.resize(2,3)
print(array5)
# %%
#stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# vertical stacking

array3 = np.vstack((array1,array2))
print(array3)

# horizontal stacking

array4 = np.hstack((array1,array2))
print(array4)

# %%

# convert and copy array
#convert

liste = [1,2,3,4]

array = np.array(liste) # liste'den arraye donusturmek
liste2 = list(array)    # array'den listeye donusturmek

#copy

a = np.array([1,2,3])
b = a
c = a
b[0] = 5
print(a)
print(b)
print(c)

d = np.array([1,2,3])
e = d.copy()
f = d.copy()
f[0] = 5
print(d)
print(e)
print(f)
print("end of the numpy")








































































