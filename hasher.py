import hashlib
import base64

def hash_it(it):
	it = 'IEEE' + it + 'Xtreme'
	return base64.b64encode(hashlib.sha256(it).digest())

def action():
	f = open('hashes.txt','r')
	hashes = [x[:-1] for x in f.readlines()]
	f.close()
	f = open('finding.txt','a')
	sample= open('sample.txt','r')
	samples = [x[:-1] for x in sample.readlines()]
	# c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
	# 	'1','2','3','4','5','6','7','8','9','0']
	for i in samples:

		# s=turn(i,c)
		# print s
		check(hashes,f,i[::-1])
	f.close()
	sample.close()

def turn(i,c):
	s = ''
	while i>0:
		s=s+(c[i%36])
		i = i/36
	return s

def check(hashes,f,i):
	if hash_it(str(i)) in hashes:
		print (str(i),"hurray")
		f.write(str(i)+'\n')

def clean():
	f = open('finding.txt','r')
	alldata = [x[:-1] for x in f.readlines()]
	f.close()
	alldata = list(set(alldata))
	f = open('finding.txt','w')
	for i in alldata:
		f.write(i+'\n')
	f.close()

def create():
	f = open('finding.txt','r')
	alldata = [x[:-1] for x in f.readlines()]
	f.close()
	alldata = list(set(alldata))
	f = open('dic.txt','w')
	f.write("dic = {")
	for i in alldata:
		f.write('"'+hash_it(i)+'":"'+i+'",')
	f.write("}")
	f.close()

def main():
	dic = {"aJIH+q0YjYZCpierKtbue5JDtZSF8tKxVKuHYUPQ65k=":"binary2","tDdmKQpMiVDFA1YdblkHSFzL4Z9UIQ9FSouf3TybOu0=":"password1","IDB/pOthrWobzapJ/N8HsraNhwfbExAa2uusdiKHFFI=":"p4ssw0rd9","8cdgZu9dBOrcTBMqElM+y9Vh5FTBRQ7n9EGa/4qVHUk=":"snakes","FFXy3vru2D8rTWZRlh9lSMvtEusfWgO17OmJCTQTECs=":"","9DS4orbhPFbjJcosEqQg+eg0Si5qSOnftfHiqK8sYug=":"voyage8","JCmqBN0MsW13tEmsQPYWg9Fj25MUrqFYvSK2arxTt0A=":"4rt5","y+zbMpySKY+WF97KkgRQ+tBpM7iTqTj9guWmGJcqfyA=":"minimum8","8OtpJ+E1XHv2RDsKIEwJc9KUFwPRzaqeHJ735Er6AVE=":"rice","RVfhsLovxa+/6tWgeSBASIIkzXkVtDPT4yYvjboHhIk=":"metric0","rdALvOYVhA3hnUTBlaQXigWBSgMYzGTreSKyMoAoKfw=":"character1","YzSqlQTtq5j+Kd+hW1ISgBW0mn61vsQsxNeipq0sYCo=":"tac04","81X3NN5JgTuGgqq3ErF0eL/l/wZFYkCwur6fZ06L2Us=":"sad6","YollqBlewcxE/kF6PKvv0r1CLZkKx82657bB0eQbiK0=":"dice9","h84yifAWGLj9sakEqxZ3QEjkXL42AoScP3L5Tdevm98=":"1","/PtjJboZGlsmTovvyOhBOoTVnQKUP/gJXxjLAW9Lppw=":"bon8","usg8BTtSfewL5M3OVg91TJCTc5vONLqgUCC/Si1Grsg=":"engineers0","Lqxt1UjT1ecV6ucgYn+yrGSUTxPWkZgdDtbygGwC/BA=":"world4","CornANxoZ5FJnlhwHmK42CDXf3h6jFr3g73YIRuoymQ=":"c4v35","j2GTUqtqZpotY8wF16zkvnbdCLTnX3oOZ30SjQUnIUk=":"formatted","GsXTQM0w+Clb1c9B7n28mADU2quLeI1n91KTyBboeHI=":"url5","lUfxHX9xH2aOHheMMqQF+f5BNh97avew2uOwEN3B7HE=":"0","r6BN0tdyAYZD0Nmc7bfV0WRcFBb1A2WIPPKHVRG59k8=":"3","BjQiH/A2FUNHlUwhBi8NWmj3HmhmAh6Ag0kRyVSaVo8=":"gold0","28AdfW0JHmCP4TbieGON8dafRaFpUgpzuX2bHZN6WsM=":"4","05HwH93tksb69U1ifesCQuYFP+gKPVH2L6W8JeBdXy0=":"digital","LZIzmWEqXDPJsnKttFGRaG/jUhHrbTEKt1XCO6XbdME=":"be2","IxQxcFXR51q8h8FLblPhYfUR30lIAt6hX8TjZWVa/GE=":"crashing","KudA8vCEQdGaaCSxotpAcluXnVPS3MAZPkwI/lVupak=":"game9","TInfNYwXvofBA+9QIe3+XEfDpO5ER+R+Jn3BOshhZWU=":"maze3","m0IeuugWDOl9cFUFRYJhouCBT39T0dpp1xBOKPqHP94=":"land6","3uDaglIdYUn11AadEhELBjE15A0L6hAaWnZmjCGtt+M=":"demons8","ix+0IJIpLpHeSHEII+Q/IVY+FlRXn3xMA0ey6UITi34=":"bst","hEGKCiTZSA5x560hodRoIBBTE8pv4sP1VXG4D0fXWcI=":"optimal2","O9L1ZWYwuzgaImTjOwuogXfpC+C44zzcDhpt08LjR5c=":"chocolate","R/ye+L9W+l6hyZ/v1POsWYboEGemIisARL8ohUvfBLI=":"bunnies","R1v9fEb9VrZuU5xiYTKTqhHF03VtXg7+KtfFHPkQuCQ=":"cow3","HWv9gx+GL/6g+0b0eOc+1Z/8BHse91/5T/DdiDwEknU=":"xtreme4","wEtqAs8JHjicWnXshAWF5Sg6NoswuG9qeJ7USw7YD7c=":"multiple3","NmrOUzHxKSfNT8UJ1YXbRL8I+HCAb+glJ0bBXcHfagE=":"art1","rwvmTDiJxIEETbsngvpxYGwZZK+FGo7527odGuQUjtQ=":"stand4","zqKPAOt5ziHSeRxc0TgUZF3rJxzBHAKdJeccvt3F7Jg=":"stand5","N5aunKGHeN2WETLXLzfhfCxAfkwtGU/imziiTF3t7oY=":"e","ugcIIpDID0R1uFqBAcN3PNXhwlhen77GdAccFgpbs+A=":"roaming7","Rz38Ng2qI3mPkaRB6uDoCYmmfzbVTCzpt2sG1o+TZqo=":"o","3hoie8omUyvM/9Qfx9dKfoptlwemYe2os8aohTGzoyw=":"i","rjwtKqkPc7cfQ+zZ+E9c+fzQYhRvhVtaKEFb+srIHcQ=":"u","FGkqFC/jLDqDZ10fql1nGw7AQNWioOrZ3ydEaJyXBwo=":"me4t4","Wau4ReopjFKk8SYYNq5lIBL+Rgg8aBR6h9UgTIv2u7I=":"b4r4","B2E/K/DywbLEKutOKpS8HxHFrZwucwac4KjzYgsXg3g=":"real7","socJeO02bT2w+XZUrLoopbZvQ1lRhDfE88GVrJQ8p+g=":"square7"}
	instr = raw_input()
	print dic[instr]

action()

clean()

create()

# main()
