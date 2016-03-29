#!/usr/bin/env python3
def f():
	ans=[]
	while 1:
		ans.insert(0,1)
		for x in range(1,len(ans)-1):
			ans[x]=ans[x]+ans[x+1]
		yield(ans)
o=f()
for x in range(10):
	print(next(o))

