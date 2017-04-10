'''This is a guess the number game.'''

import random

guessesTaken = 0

print ("Hello! What is your name?")
myName = input()

number = random.randint(1,30)
print( "We'll %s, I am thinking of a number between 1 and 30" %myName)

while guessesTaken < 10:
	print ("Take a guess.")
	guess = input()
	guess = int(guess)

	guessesTaken += 1

	if guess < number:
		print ("Your guess is too low!")

	if guess > number:
		print( "Your guess is too high!")

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print( "Good job %s! You guessed my number in %s guesses!" %(myName, guessesTaken))

if guess != number:
	number = str(number)
	print ("Nope. The number I was thinking of was %s" %number)


