def action():
	tests = input()
	for test in range(tests):
		inp = [x for x in (raw_input().split())]
		switches = long(inp[0])
		grmlins = int(inp[1])
		primes = {}
		for g in range(grmlins):
			primes[g] = int(inp[g+2])
		count = 0
		for num in range(1,(2**grmlins)):
			val,mul = tonum(num,primes)
			count = count + mul*(switches/val)
			# print switches/val
		print count/2

def tonum(num,primes):
	val = 1
	mul = -1
	for i in primes.keys():
		if (num/(2**i))%2==1:
			mul = -2*mul
			val = val * primes[i]
	# print num,val,mul
	return val,mul

action()
