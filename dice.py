#dice

#4 6 8 10 12 20

#input in format 3d10+2 meaning 3 rolls of a 10 sided dice

import sys, os, random

def gen_nums():
	nums = []
	for x in range(0, 10):
		nums.append(str(x))
	return nums

def dice(rolls, sides, denominator = 1, offset = 0):
	
	total = 0
	for i in range(0, rolls):
		x = random.randint(1, sides)
		print "roll{0} of {1} = {2}".format(i + 1, rolls, x)
		total += x
	total = float(total) / float(denominator)
	total = int(total)
	total += offset
	print total
		
while True:
	str = raw_input()
	selection = 0
	for i in range(0, 4)
		for char in str:
			data = ""
			if char == ",":
				break
			if char in gen_nums():
			
			
	dice(x)
	selection = 0