import random, os, time

guessed = False
tries = 0
print("Please enter maximum number: ")
maxNum = input("> ")
maxNum = int(maxNum)

number = random.randint(0, maxNum)

print("Maximum number set to : " + str(maxNum) + ".")
time.sleep(2)
os.system("cls")
print("Type Exit at anytime to Exit.")

while not guessed:
	guess = input("Your guess> ")
	
	if int(guess) == number:
		print("You won on your " + str(tries) + "th try!")
		tries = tries + 1
		guessed = True
		os.system("pause")
		os.system("cls")

	if int(guess) < number:
		print("Wrong, your guess was too low!")
		tries = tries + 1

	if int(guess) > number:
		print("Wrong, your guess was too high!")
		tries = tries + 1