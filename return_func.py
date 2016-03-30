#!/usr/bin/env python3
def count():
	fs=[]
	for i in range(4):
		def f():
			return i**2
		fs.append(f)
	return fs
for f in count():
	print(str(f),str(f()))
