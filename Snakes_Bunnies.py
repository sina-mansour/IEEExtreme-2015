def action():
	size = input()
	vol = size**2
	board = {}
	walker = vol
	for i in range(size):
		line = raw_input()
		if i%2==0:
			line = line[::-1]
		while (len(line)>0):
			board[walker]=line[0]
			line=line[1:]
			walker=walker-1
	# print 'board is ready'
	jumps = alljumps(board)
	mod = input()
	player = 0
	positions={}
	while True:
		player = player+1
		try:
			dice1 = input()
			dice2 = input()
			# print '2 reads'
			result = play(dice1+dice2,positions,jumps,player)
			if result == -1:
				print ('PLAYER '+str(player)+' WINS BY EVIL CYCLE!')
				break
			if result>=vol:
				positions[player]=vol
				poslist = []
				for i in range(mod):
					poslist.append(str(positions.get((mod+1),0)))
				word = ' '.join(poslist)
				print word
				break
			positions[player]=result
			# print ('play' + str(player))
			# print (positions)
			if (dice1==dice2):
				dicex = input()
				# print '1 read'
				result = play(dicex,positions,jumps,player)
				if result == -1:
					print ('PLAYER '+str(player)+' WINS BY EVIL CYCLE!')
					break
				if result>=vol:
					# print 'here'
					positions[player]=vol
					poslist = []
					for i in range(mod):
						player = i+1
						poslist.append(str(positions.get((player),0)))
					word = ' '.join(poslist)
					print word
					break
				positions[player]=result
				# print ('play extra' + str(player))
				# print (positions)
				# play extra
		except EOFError:
			# print 'except'
			poslist = []
			for i in range(mod):
				player = i+1
				poslist.append(str(positions.get((player),0)))
			word = ' '.join(poslist)
			print word
			break
		player = player%mod

def play(dice, positions, jumps, player):
	current = positions.get(player,0)
	if current!=0:
		del positions[player]
	after = trance(current+dice,positions,jumps,[])
	return after

def trance(land, positions, jumps, const):
	if jumps.get(land,False):
		return trance(jumps[land], positions, jumps, const+[land])
	if land in const:
		return -1
	if land in positions.values():
		return trance(land+1, positions, jumps, const+[land])
	return land

def alljumps(board):
	jumps={}
	for start in range(1,len(board.keys())+1):
		if board[start].isdigit():
			# bunnies
			for end in range(start+1,len(board.keys())+1):
				if board[start]==board[end]:
					jumps[start]=end
		if board[start].islower():
			# snakes
			for end in range(start+1,len(board.keys())+1):
				if board[start]==board[end]:
					jumps[end]=start
	return jumps

action()
