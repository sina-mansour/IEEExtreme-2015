
# from __future__ import generators

def action():
	tests = input()
	for test in range(tests):
		sample = raw_input()
		pat = sample[0]
		patlen = 1
		shifts = makes(pat)
		# for i in range(len(sample)):
		i=0
		while i<len(sample):
			if sample[i]!=sample[i%patlen]:
				patlen=patlen+shifts[i%patlen]
				shifts = makes(sample[:patlen])
				i = patlen - 1
				# print sample[:patlen]
			i = i+1
		print patlen

def makes(pattern):
	# build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    return shifts


# def KnuthMorrisPratt(text, pattern):
#     # allow indexing into pattern and protect against change during yield
#     pattern = list(pattern)

#     # build table of shift amounts
#     shifts = [1] * (len(pattern) + 1)
#     shift = 1
#     for pos in range(len(pattern)):
#         while shift <= pos and pattern[pos] != pattern[pos-shift]:
#             shift += shifts[pos-shift]
#         shifts[pos+1] = shift

#     # do the actual search
#     startPos = 0
#     matchLen = 0
#     for c in text:
#         while matchLen == len(pattern) or \
#               matchLen >= 0 and pattern[matchLen] != c:
#             startPos += shifts[matchLen]
#             matchLen -= shifts[matchLen]
#         matchLen += 1
#         if matchLen == len(pattern):
#             yield startPos

# makes('abc')
# calc('abcaa')
action()
