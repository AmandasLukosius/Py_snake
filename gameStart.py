import functions as f

class gameStart():
	# Greet new player
	def greetings():
		message = 'Hello stranger! \nThis is SNAKE GAME! \nControls: w - up, s - down, a - left, d - right\n'
		f.functions.write_text(message)