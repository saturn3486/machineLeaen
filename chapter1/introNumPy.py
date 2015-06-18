# -*- coding:utf-8 -*-
import numpy as np
#numpy is conflict with array of python standard probably 
print np.version.full_version

#not using [from numpy import *] to not conterminate name space

a = np.array([0,1,2,3,4,5])
print a

"""print a.ndim
#number of dimensions
print a.shape
#touple of array dimensions

b = a.reshape((3,2))
print b
print b.ndim
print b.shape

b[1][0] = 77
print b
print a
#a become the same as fixed b.

c = a.reshape((3,2)).copy()
#copy() is require to duplicate array instance.
print c
print c.ndim
print c.shape

c[1][0] = 101
print c
print a
"""
"""
print a*2
b = a<4
print b

a[a<4]=0
b = a<4
print b,a
"""

print a.clip(2,4)