def action():
	[r,c] = [int(x) for x in (raw_input().split())]
	canvas = {}
	for i in range(r):
		for j in range(c):
			canvas[i+1,j+1]=0
	n = input()
	for line in range(n):
		[operation,tlr,tlc,brr,brc] = [x for x in (raw_input().split())]
		tlr = int(tlr)
		tlc = int(tlc)
		brr = int(brr)
		brc = int(brc)
		if operation == 'a':
			for i in range(tlr,brr+1):
				for j in range(tlc,brc+1):
					canvas[i,j] = canvas[i,j] + 1;
		elif operation == 'r':
			for i in range(tlr,brr+1):
				for j in range(tlc,brc+1):
					canvas[i,j] = canvas[i,j] - 1;
		elif operation == 'q':
			count = 0
			for i in range(tlr,brr+1):
				for j in range(tlc,brc+1):
					count = count + canvas[i,j];
			print (count)

action()
