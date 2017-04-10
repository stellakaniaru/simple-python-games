import random

'''CHECK ON THR ASSCII ART OUTPUT!'''

HANGMANPICS = ['''
	+ --- +

	|    |

	     |

	     |

	     |

	     |
	------------
	------------''' , '''
	+ --- +

	|	 |

	O	 |

		 |

		 |

		 |
	------------
	------------''' , '''

	+ --- +

	|    |

	O    |

	|    |

	     |

	     |
	------------
	------------''' , '''

	+ --- +

	|    |

	O    |

   /|    |

	     |

	     |
	------------
	------------''' , '''

	+ --- +

	|    |

	O    |

   /|\   |

	     |

	     |
	------------
	------------''' , '''

	+ --- +

	|    |

	O    |

   /|\   |

  /     |

	     |
	------------
	------------''' , '''

	+ --- +

	|    |

	O    |

   /|\   |

   / \   |

	     |
	------------
	------------''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weael whale wolf wombat zebra'.split()

def getRandomWord(wordlist):
	'''Returns random string from passed list of strings'''
	#generates a random index from word list
	wordIndex = random.randint(0, len(wordlist) - 1)
	#returns the word in the randomly generated index
	return wordlist[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	'''Prints the hangman board on the screen and how many letters the user has correctly
	and incorrectly spelt.'''
	#HANGMANPICS displays the board as art.
	#missedLetters show a string of letters the player has guessed and are not in the secretWord
	#correctLetters show a string of letters the player has guessed and are in the secretWord
	#secretWord shows a string of the secretWord a player is trying to guess.
	print (HANGMANPICS[len(missedLetters)])
	print ()

	print('Missed letters: ', ' ')
	for letter in missedLetters:
		print (letter, '')
	print ()

	blanks = '_' * len(secretWord)

	for i in range(len(secretWord)):
		#replace blanks with correctly guessed latters
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

	for letter in blanks:
		#show the secret word with spaces in between each letter
		print(letter, ' ')
	print ()

def getGuess(alreadyGuessed):
	'''Returns the letter the player entered.Makes sure
	the player enters a single letter,not something else.'''
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print ('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess

def playAgain():
	'''Returns True if the player wants to play again,
	otherwise it returns False.'''

	print('Do you want to play again?(yes or no)')
	return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

	#let the player type in a letter
	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess

		#check if player has won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is ' + secretWord + ' You have won!')

			gameIsDone = True

	else:
		missedLetters = missedLetters + guess 

		#check if player has guessed too many times and lost
		if len(missedLetters) == len(HANGMANPICS) - 1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

			print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + ' "')

			gameIsDone = True

#ask the player if they want to play again(but only if the game is done)
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break

