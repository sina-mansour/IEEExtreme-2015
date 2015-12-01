# left loses
wins={'Scissors':['Paper','Lizard'], 'Paper':['Rock','Spock'], 'Rock':['Lizard','Scissors'], \
		'Lizard':['Spock','Paper'], 'Spock':['Scissors','Rock']}
# left wins
loses={'Scissors':['Spock','Rock'], 'Paper':['Scissors','Lizard'], 'Rock':['Paper','Spock'], \
		'Lizard':['Rock','Scissors'], 'Spock':['Lizard','Paper']}

def action():
	tests = input()
	for test in range(tests):
		[alice,bob,n] = [x for x in (raw_input().split())]
		past = {(alice,bob):(0,0,0,0)}
		rounds=0
		left=int(n)
		bw=0
		aw=0
		tt=0
		getin = True 
		while True:
			if left > 0:
				# tied
				if bob == alice:
					bob,alice = bobnext(bob,'tie'),alicenext(alice,bob,'tie')
					tt = tt +1
				# bob loses
				elif bob in wins[alice]:
					bob,alice = bobnext(bob,'lose'),alicenext(alice,bob,'win')
					aw = aw + 1
				# bob wins
				elif alice in wins[bob]:
					bob,alice = bobnext(bob,'win'), alicenext(alice,bob,'lose')
					bw = bw + 1
				left = left - 1
				rounds = rounds + 1
			# print ("rounds: ",rounds," left: ",left)
			# print past
			# print (alice,bob)
			if left <= 0:
				result(bw,aw,tt)
				break
			if rounds < 1000:
				if ((alice,bob) in past.keys()) and getin:
					# print 'in'
					# getin = False
					loop,aaw,bbw,ttt = past[(alice,bob)] 
					div = (rounds-loop)
					# if div == 0:
					# 	print (rounds,loop)
					mul = (left/div)
					left,rounds = (left % div),(rounds + left - (left % div))
					bw = bw + mul * (bw-bbw)
					aw = aw + mul * (aw-aaw)
					tt = tt + mul * (tt-ttt)
					# print 'out'
				else:
					past[(alice,bob)]=(rounds,aw,bw,tt)

def result(bw,aw,tt):
	if bw==aw:
		print ('Alice and Bob tie, each winning '+str(bw)+' game(s) and tying '+str(tt)+' game(s)')
	elif bw>aw:
		print ('Bob wins, by winning '+str(bw)+' game(s) and tying '+str(tt)+' game(s)')
	elif bw<aw:
		print ('Alice wins, by winning '+str(aw)+' game(s) and tying '+str(tt)+' game(s)')

def alicenext(alice,bob,sit):
	if sit == 'win':
		return alice
	elif sit == 'tie':
		return loses[alice][0]
	elif sit == 'lose':
		return loses[bob][0]

def bobnext(bob,sit):
	if bob != 'Spock':
		return 'Spock'
	else:
		if sit == 'tie':
			return 'Lizard'
		elif sit == 'win':
			return 'Rock'
		elif sit == 'lose':
			return 'Paper'

action()
