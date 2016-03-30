#!/usr/bin/env python3

def hello():
	print('Welcome!')

def decorator(myfunc,orifunc):
	def wrapper(*args,**kw):
		myfunc()
		return orifunc(*args,**kw)
	return wrapper

abs=decorator(hello,abs)
print(abs(-1))

# a simple example of using a decorator
# 3-layered structure decorator may be used if myfunc() has variables

