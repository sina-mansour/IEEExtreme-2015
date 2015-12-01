def action():
	tests = input()
	for test in range(tests):
		X = input()
		Y = 2
		L = 2
		D = 'H'
		Boxes = [[L,D,X,Y]]
		N = input()
		B = input()
		for i in range(B):
			[s,d,c,r] = [x for x in (raw_input().split())]
			Boxes.append([int(s),d,int(r),int(c)])
		t = 0
		states = []
		states.append(Boxes)
		# print Boxes
		final=False
		nBoxes=[]
		pBoxes=[]
		while True:
			t = t + 1
			# print t
			for state in states:
				for i in range(len(state)):
					for m in moves(state[i],N):
						nb=(state[:i]+[m]+state[i+1:])
						if (nb not in states+pBoxes+nBoxes) and (isright(nb)):
							# print nb
							nBoxes.append(nb)
							[l,d,x,y]=nb[0]
							if x + l == N:
								final = True
								print t
								break
					if final:
						break
				if final:
					break
			pBoxes = states
			states = nBoxes
			nBoxes = []
			if final:
				break
			

def conflict(b1,b2):
	[l1,d1,x1,y1] = b1
	[l2,d2,x2,y2] = b2
	if d1 == d2:
		if d1=='V' and x1==x2:
			if (y1==y2+l2-1 or y2==y1+l1-1):
				return True
		elif d1=='H' and y1==y2:
			if (x1==x2+l2-1 or x2==x1+l1-1):
				return True
	else:
		if d1=='V':
			if x1>=x2 and x1<=x2+l2-1 and y2>=y1 and y2<=y1+l1-1:
				return True
		else:
			if x2>=x1 and x2<=x1+l1-1 and y1>=y2 and y1<=y2+l2-1:
				return True
	return False

def isright(Boxes):
	for i in range(len(Boxes)):
		for j in range(i+1,len(Boxes)):
			if conflict(Boxes[i],Boxes[j]):
				# print ('conflict: ',Boxes[i],Boxes[j])
				return False
	return True

def nextBoxes(Boxes,N):
	nBoxes=[]
	for i in range(len(Boxes)):
		for m in moves(Boxes[i]):
			nBoxes.append(Boxes[:i]+[m]+Boxes[i+1:])
	return nBoxes

def moves(box,N):
	mvs = []
	[l,d,x,y]=box
	if d=="V":
		if y>0:
			mvs.append([l,d,x,y-1])
		if y+l<N:
			mvs.append([l,d,x,y+1])
	else:
		if x>0:
			mvs.append([l,d,x-1,y])
		if x+l<N:
			mvs.append([l,d,x+1,y])
	return mvs

action()
