def action():
	# precomputations:
	start_end={(1,1,10**6):656373268,(1,2,10**6):913435099,(1,3,10**6):297125695,(1,4,10**6):738282009,\
				(2,1,10**6):913435099,(2,2,10**6):953498963,(2,3,10**6):651717101,(2,4,10**6):297125695,\
				(3,1,10**6):297125695,(3,2,10**6):651717101,(3,3,10**6):953498963,(3,4,10**6):913435099,\
				(4,1,10**6):738282009,(4,2,10**6):297125695,(4,3,10**6):913435099,(4,4,10**6):656373268,\
				(1,1,10**8):476955330,(1,2,10**8):350076791,(1,3,10**8):313185733,(1,4,10**8):568495199,\
				(2,1,10**8):350076791,(2,2,10**8):790141063,(2,3,10**8):918571990,(2,4,10**8):313185733,\
				(3,1,10**8):313185733,(3,2,10**8):918571990,(3,3,10**8):790141063,(3,4,10**8):350076791,\
				(4,1,10**8):568495199,(4,2,10**8):313185733,(4,3,10**8):350076791,(4,4,10**8):476955330,\
				(1,1,10**10):467157440,(1,2,10**10):423032243,(1,3,10**10):315111771,(1,4,10**10):651708029,\
				(2,1,10**10):423032243,(2,2,10**10):782269211,(2,3,10**10):74740265,(2,4,10**10):315111771,\
				(3,1,10**10):315111771,(3,2,10**10):74740265,(3,3,10**10):782269211,(3,4,10**10):423032243,\
				(4,1,10**10):651708029,(4,2,10**10):315111771,(4,3,10**10):423032243,(4,4,10**10):467157440,\
				(1,1,10**12):443553884,(1,2,10**12):164070412,(1,3,10**12):185824201,(1,4,10**12):712858642,\
				(2,1,10**12):164070412,(2,2,10**12):629378085,(2,3,10**12):876929054,(2,4,10**12):185824201,\
				(3,1,10**12):185824201,(3,2,10**12):876929054,(3,3,10**12):629378085,(3,4,10**12):164070412,\
				(4,1,10**12):712858642,(4,2,10**12):185824201,(4,3,10**12):164070412,(4,4,10**12):443553884,\
				(1,1,10**14):487111129,(1,2,10**14):198097797,(1,3,10**14):981324711,(1,4,10**14):222809211,\
				(2,1,10**14):198097797,(2,2,10**14):468435833,(2,3,10**14):420907008,(2,4,10**14):981324711,\
				(3,1,10**14):981324711,(3,2,10**14):420907008,(3,3,10**14):468435833,(3,4,10**14):198097797,\
				(4,1,10**14):222809211,(4,2,10**14):981324711,(4,3,10**14):198097797,(4,4,10**14):487111129,\
				(1,1,10**16):464497832,(1,2,10**16):171011576,(1,3,10**16):196904854,(1,4,10**16):953774091,\
				(2,1,10**16):171011576,(2,2,10**16):661402686,(2,3,10**16):124785660,(2,4,10**16):196904854,\
				(3,1,10**16):196904854,(3,2,10**16):124785660,(3,3,10**16):661402686,(3,4,10**16):171011576,\
				(4,1,10**16):953774091,(4,2,10**16):196904854,(4,3,10**16):171011576,(4,4,10**16):464497832,\
				(1,1,10**4):590847951,(1,2,10**4):145837266,(1,3,10**4):393110198,(1,4,10**4):319351591,\
				(2,1,10**4):145837266,(2,2,10**4):983958149,(2,3,10**4):465188857,(2,4,10**4):393110198,\
				(3,1,10**4):393110198,(3,2,10**4):465188857,(3,3,10**4):983958149,(3,4,10**4):145837266,\
				(4,1,10**4):319351591,(4,2,10**4):393110198,(4,3,10**4):145837266,(4,4,10**4):590847951,\
				(1,1,10**2):849264838,(1,2,10**2):631811249,(1,3,10**2):537602337,(1,4,10**2):161269656,\
				(2,1,10**2):631811249,(2,2,10**2):386867168,(2,3,10**2):793080905,(2,4,10**2):537602337,\
				(3,1,10**2):537602337,(3,2,10**2):793080905,(3,3,10**2):386867168,(3,4,10**2):631811249,\
				(4,1,10**2):161269656,(4,2,10**2):537602337,(4,3,10**2):631811249,(4,4,10**2):849264838}
	mod = 10**9 + 7
	[length,count] = [int(x) for x in (raw_input().split())]
	# [length,count] = [10**2,0]
	cows = {}
	ways = {}
	for line in range(count):
		[x,y] = [int(x) for x in (raw_input().split())]
		cows[(x,y)] = True
	if cow_block(cows):
		print 0
		return
	# test:
	# end = input("end lane?\n")
	# start = input("start lane?\n")
	end = 1
	start = 1
	ways[(end,length)] = 1
	unit = length
	while unit>0:
		if unit>10**16 and no_cows_near((unit-10**16+1),unit,cows):
			past=unit
			unit=unit-10**16+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**16)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**16)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**16)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**16)]) % mod
		elif unit>10**14 and no_cows_near((unit-10**14+1),unit,cows):
			past=unit
			unit=unit-10**14+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**14)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**14)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**14)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**14)]) % mod
		elif unit>10**12 and no_cows_near((unit-10**12+1),unit,cows):
			past=unit
			unit=unit-10**12+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**12)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**12)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**12)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**12)]) % mod
		elif unit>10**10 and no_cows_near((unit-10**10+1),unit,cows):
			past=unit
			unit=unit-10**10+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**10)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**10)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**10)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**10)]) % mod
		elif unit>10**8 and no_cows_near((unit-10**8+1),unit,cows):
			past=unit
			unit=unit-10**8+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**8)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**8)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**8)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**8)]) % mod
		elif unit>10**6 and no_cows_near((unit-10**6+1),unit,cows):
			past=unit
			unit=unit-10**6+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**6)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**6)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**6)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**6)]) % mod
		elif unit>10**4 and no_cows_near((unit-10**4+1),unit,cows):
			past=unit
			unit=unit-10**4+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**4)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**4)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**4)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**4)]) % mod
		elif unit>10**2 and no_cows_near((unit-10**2+1),unit,cows):
			past=unit
			unit=unit-10**2+1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((1,past),0)*start_end[(lane,1,10**2)] + \
										ways.get((2,past),0)*start_end[(lane,2,10**2)] + \
										ways.get((3,past),0)*start_end[(lane,3,10**2)] + \
										ways.get((4,past),0)*start_end[(lane,4,10**2)]) % mod
		else:
			unit = unit-1
			for lane in range(1,5):
				if not cows.get((lane,unit),False):
					ways[(lane,unit)] = (ways.get((lane,unit+1),0) + \
										ways.get((lane+1,unit+1),0) + \
										ways.get((lane-1,unit+1),0)) % mod
	print (ways.get((start,1),0))

def no_cows_near(i,i106,cows):
	pos = cows.keys()
	for x,y in pos:
		if y>=i and y<=i106:
			return False
	return True

def cow_block(cows):
	pos = cows.keys()
	while (len(pos)>0):
		cow = pos[0]
		block = related([cow],pos)
		if fits(block):
			return True
		for cow in block:
			pos.remove(cow)
	return False

def fits(cows):
	lane = {1:False,2:False,3:False,4:False}
	for x,y in cows:
		lane[x]=True
	if False not in lane.values():
		return True
	return False

def related(cows,pos):
	rltd = cows
	grow = False
	for cow in cows:
		arnd = around(cow,pos)
		for c in arnd:
			if c not in rltd:
				grow = True
				rltd.append(c)
	if grow == False:
		return rltd
	else:
		return related(rltd,pos)


def around(cow,cows):
	x,y = cow
	arnd=[]
	if (x-1,y) in cows:
		arnd.append((x-1,y))
	if (x+1,y) in cows:
		arnd.append((x+1,y))
	if (x,y-1) in cows:
		arnd.append((x,y-1))
	if (x,y+1) in cows:
		arnd.append((x,y+1))
	return arnd


action()
