import math, time, random, sys, os
playerWins = 0
cpuWins = 0
gameCount = 0
finished = False
gameFinished = False

while not finished:

	print("How many games would you like to play?\nPlease give an odd number greater than 3 and less than 15.")
	numOfGames = input("> ")

	if numOfGames % 2 == 0 or numOfGames < 3 or numOfGames > 15:
		print("Invalid number, please make sure it is an odd number greater than 3 and less than 15.")
	else:
		print("Number of games set.")
		time.sleep(2)
		os.system("cls")
		finished = True

numOfWinsNeeded = int(math.ceil(numOfGames / 2.0))

print("Can you beat the CPU " + str(numOfWinsNeeded) + " times out of " + str(numOfGames) + "?")
#Let's start the game
print("--------------------------------------\n")
print("Type 'options' at any time to see available options.")

while not gameFinished:
	cpuAnswers = ["rock", "paper", "scissors"]

	cpuAnswer = random.choice(cpuAnswers)

	userAnswer = raw_input("Rock, Paper, or Scissors> ")
	userAnswer = userAnswer.lower()

	if userAnswer == cpuAnswer:
		print("Computer guessed " + cpuAnswer + " too! Try again.")
		gameCount = gameCount + 1
	#Rock
	elif userAnswer == "rock":
		gameCount = gameCount + 1

		if cpuAnswer == "scissors":
			print("Computer answer is scissors, you win this round!")
			playerWins = playerWins + 1
		elif cpuAnswer == "paper":
			print("Computer answer is paper, you lose this round!")
			cpuwins = cpuWins + 1
	#Paper		
	elif userAnswer == "paper":
		gameCount = gameCount + 1

		if cpuAnswer == "rock":
			print("Computer answer is rock, you win this round!")
			playerWins = playerWins + 1
		elif cpuAnswer == "scissors":
			print("Computer answer is scissors, you lose this round!")
			cpuWins = cpuWins + 1
	#Scissors
	elif userAnswer == "scissors":
		gameCount = gameCount + 1

		if cpuAnswer == "paper":
			print("Computer answer is paper, you win this round!")
			playerWins = playerWins + 1
		elif cpuAnswer == "rock":
			cpuWins = cpuWins + 1
			print("Computer answer is rock, you lose this round!")

	elif userAnswer == "options":
		print("Exit -- Exits the game.")
		print("Score -- Displays score.")
		print("Count -- How many games have been played.")

	elif userAnswer == "exit":
		print("Goodbye.")
		time.sleep(2)
		sys.exit()

	elif userAnswer == "score":
		print("Player wins: " +str(playerWins))
		print("Computer wins: " +str(cpuWins))

	elif userAnswer == "count":
		print("Playing game " + str(gameCount) + " of " +str(numOfWinsNeeded))

	else:
		print("Wat.")

	if playerWins == numOfWinsNeeded:
		gameFinished = True
		os.system("cls")
		print("Player wins!\n")
		print("Final score:\n")
		print("You: "+ str(playerWins) + " Computer: " +str(cpuWins))
	if cpuWins == numOfWinsNeeded:
		gameFinished = True
		os.system("cls")
		print("Computer wins!\n")
		print("Final score:\n")
		print("Computer: "+ str(cpuWins) + " You: " +str(playerWins))