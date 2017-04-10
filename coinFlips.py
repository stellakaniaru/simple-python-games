'''
Simulates the flipping of a coin 1000 times.
User has to guess how many times heads will come up.
'''

import random
print( "I will flip a coin 10 times. Guess how many times it will come up heads. Press enter to begin.")
input(' ')

flips = 0
heads = 0

while flips < 10:
	if random.randint(0, 1) == 1:
		heads += 1
	flips += 1

	if flips == 2:
		print( "2 flips and there have been "+ str(heads) + " heads")

	if flips == 4:
		print ("At 4 tosses, heads has come up "+ str(heads) + " times so far.")

	if flips == 5:
		print ("Half way done and heads has come up "+ str(heads) + " times.")

print()
print ("Out of 10 coin tosses, heads came up %d times!" % heads)