def action():
	# [n,d] = [int(x) for x in (raw_input().split())]
	n =input()
	d =input()
	# bar = [[0 for x in range(d)] for x in range(n)]
	bar = {}
	# sumall=0
	for i in range(n):
		for j in range(d):
			bar[i,j]=bar.get((i-1,j),0)+bar.get((i,j-1),0)+(2**(i+j))
			# sumall = sumall + bar[i,j]
	print bar[n-1,d-1]

def calc(i,j,bar):
	val = 1
	for i1 in range(i):
		val = val + bar[i1,j]
	for j1 in range(j):
		val = val + bar[i,j1]
	for i1 in range(i):
		for j1 in range(j):
			val = val + bar[i1,j1]
	return val

action()
