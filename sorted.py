#!/usr/bin/env python3

# This is a function that simulates the origin of sorted()
# You have to check the variables in the def of the function

from collections import Iterable
def fun(i,*,key=None,reverse=False):
	if not isinstance(i,Iterable):
		return 'illegal'
	return str(i)+str(key)+str(reverse)

print(fun(1))
print(fun((1,)))
#fun([1],keys=abs)
print(fun((1,),key=abs))
