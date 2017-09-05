
"""
l = ['a','b','c', 'd']
ss = []

for i in l:
	if len(ss) > 0:
		for k in range(0,len(ss)):
			ss.append(ss[k]+i)
	ss.append(i)

print(ss)
def out(ss,l):
	if len(ss) > 4:
		return ss
	else:
		for i in l:
			for s in ss:
				ss.append(s+i)
		print"rerun" + ss
		out(ss,l)
		#out(ss,l)

out(ss,l)
add each item to a list
iterate through new list adding each item from old list
iterate through new list adding each item from old list
iterate through new list adding each item to old items and appending


def Hello(count):
	if count<1:
		return #base case
	print("Hello" + str(count))
	Hello(count-1)

Hello(10)
"""

l = ['a','b','c']

sps = []
def super(ss,l):
	ss = l
	stop = len(ss)
	for i in l:
		for k in range(0,stop):
			ss.append(ss[k]+i)

print (super(sps,l))