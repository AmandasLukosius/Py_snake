import colorama, random, sys
from time import sleep

class functions:

	def operation(left, op, right):
		return op(left, right)

	# Write text in fancy style
	def write_text(text):
		for c in text:
			print(random.choice(c), end=''),
			sys.stdout.flush()
			sleep(0.05)

	# Allows only awsd characters
	def getChar():
		inputChar = input("Enter: ")
		allowedChars = 'wsad'
		while(len(inputChar) != 1 or inputChar not in allowedChars):
			inputChar = input("Not allowed character was entered.\n")
		return inputChar