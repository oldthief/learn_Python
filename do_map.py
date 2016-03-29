#!/usr/bin/env python3
def normalize(name):
	return name.title()
clas=['ZhouZY','bOB','MianYang Bob']
print(list(map(normalize,clas)))

## pay attention to the four similar functions of str:
## lower() upper() capitalize() title()
