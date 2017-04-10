'''The Dragon Realm game. Its all about chances.'''

import random
import time 

def displayIntro():
	'''Displays the game's introduction statements.'''

	print ("You are in a land full of dragons. In front of you,")
	print ("you see two caves. In one cave, the dragon is friendly")
	print ("and will share his treasure with you. The other dragon")
	print ("is greedy and hungry, and will eat you on sight.")


def chooseCave():
	'''Allows a player to select the cave they wish to enter.'''
	#once the function is called,it returns the value stored in cave variable

	#variable holds an empty string
	cave = ''
	
	#input validation.The user will not be able to advance on until they type in one of the options provided
	#while loop continues to loop so long as a condition is true.
	#if the user types in one of the expected values,the while condition will evaluate to false and the loop will stop.
	while cave != '1' and cave != '2':
		print( "Which cave will you go into? (1 or 2)")
		#input is stored in cave variable as a string
		cave = input()

	#returns the value stored in cave variable
	return cave

def checkCave(chosenCave):
	'''Checks the cave chosen by player and displays outcome based on that.'''

	print ("You approach the cave...")
	
	#pauses the program for 2 seconds
	time.sleep(2)
	print( "It is dark and spooky...")
	time.sleep(2)
	print ("A large dragon jumps out infront of you! He opens his jaws and...")
	print()
	time.sleep(2)

	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print ("Gives you his treasure!")

	else:
		print ("Gobbles you down in one bite!")


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
	displayIntro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print ("Do you want to play again?(Yes or No)")
	playAgain = input()
