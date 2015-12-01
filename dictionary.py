def action():
	tests = input()
	for test in range(tests):
		[d,s] = [int(x) for x in (raw_input().split())]
		dics = []
		words = []
		perfect = {}
		for word in range(d):
			i = raw_input()
			words.append(i)
			perfect = better(perfect,todic(i))
		for dic in range(s):
			i = raw_input()
			dics.append(i)
			if isbetter(todic(i),perfect):
				# ans = 'Yes '
				if value(todic(i))>value(perfect):
					print 'Yes No'
				else:
					print 'Yes Yes'
			else:
				print "No "+str(lesser(perfect,todic(i)))


def lesser(perfect,dic):
	lesser = 0
	for i in perfect.keys():
		if perfect[i]>dic.get(i,0):
			lesser = lesser + perfect[i] - dic.get(i,0)
	return lesser

def value(dic):
	val = 0
	for i in dic.keys():
		val = val + dic[i]
	return val

def todic(word):
	dic = {}
	while len(word)>0:
		dic[word[0]]=1+dic.get(word[0],0)
		word = word[1:]
	return dic

def better(d1,d2):
	l = d1.keys()+d2.keys()
	l = list(set(l))
	dic = {}
	for key in l:
		dic[key]=max(d1.get(key,0),d2.get(key,0))
	return dic

def isbetter(d1,d2):
	l = d1.keys()+d2.keys()
	l = list(set(l))
	for key in l:
		if d2.get(key,0)>d1.get(key,0):
			return False
	return True

action()
