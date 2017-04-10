'''A game of truth or dare.'''

from sys import exit
import random
import time



def play():
	'''Initiates the game and spells out the instructions of the game.'''
	print('''
	WELCOME MATES!'
	Its time for an awesome game of TRUTH or DARE!'
	Each one in the crowd will pick a number and we\'ll do this randomly.'
	A number is be picked randomly and whoever is it will brace the HOTSEAT!'
	If you want to terminate the game, type END after the >> prompt.'
	LET THE GAMES BEGIN!
	''')
	
def guess():
	'''Depending on the number of players,randomly picks who'll be playing for each round.'''
	number = random.randint(1, num)
	print ('So, the guy on the HOTSEAT is the one with number:')
	time.sleep(3)
	print(number)
	print('LET\'S DO THIS!!!')
	print ('Teren Teren....\n')
	time.sleep(3)
	player()


def player():
	'''Randomly decides if a player gets to play a dare or a truth.'''
	fate = random.randint(1, 2)
	if fate == 1:
		print('You get TRUTH mate!\n')
		truth()
	else:
		print('You get a DARE mate!\n')
		dare()


def end():
	'''Ends the game or continues it depending on input by user.'''
	ans = input('>> ')
	if 'end' in ans:
		print ('Game up!')
		exit(0)
	else:
		print('Let\'s go another round:')
		guess()



def truth():
	'''Randomly generates a truth from a given list to ask the player.'''
	truths = ['What was your funniest date ever?',
	'What is your weirdest habit?',
	'If there was no such thing like money,what would you do with your life?',
	'What is your guilty pleasure?',
	'How many sex partners have you had?',
	'Have you ever paid for sex?',
	'If you were to win the lottery,would you drop out of school?',
	'Have you ever wet your bed as an adult?',
	'Would you rather be a horse or cow and why?',
	'If you could put someone in your life mute for a day,who would it be and why?',
	'Whats the longest youve gone without a shower?',
	'Whats the one thing you cant stand in the opposite sex?',
	'What would you do if you were the opposite sex for a whole month?',
	'Who here would you like to makeout most with?',
	]
	print('So....\n')
	time.sleep(3)
	x = random.choice(truths)
	print (x.upper())
	ans = input('Press enter to continue: ')
	print('Haha! That was something,huh?\n')
	end()


	
def dare():
	'''Randomly generates a truth from a given list to ask the player.'''
	dares = ['Apply peanut butter to one side of your face and jelly to the other',
	'Make out with a person of the opposite sex for five minutes',
	'Make an obscene call to a random person',
	'Put icecubes in your underwear for five minutes',
	'Let the group pose you in an embarrasing position and take a picture to post on your social wall',
	'Play a song by slapping your butt till someone guesses the song',
	'Sniff the armpits of everyone in the crowd',
	'Seduce a person of the same gender in the group',
	'Sing everything you say for the next ten minutes',
	'Take a selfie with the toilet and post it online',
	'Take a shower full clothed',
	'Spin the bottle and whoever it lands on,take their shirt off using your mouth only',
	'Makeout with an object the crowd chooses for five minutes.',
	'Hold your shoe up to your nose until its your turn again.']
	print('So....\n')
	time.sleep(3)
	x = random.choice(dares)
	print(x.upper())
	ans = input('Press enter to continue: ')
	print('Hahaha! Hope you had fun! Feel\'s good being evil!\n')
	end()

#initiates the game by knowing the number of people taking part	
print('How many people are playing?')
num = int(input())
play()


