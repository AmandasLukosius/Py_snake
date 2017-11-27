from operator import add, sub
from time import sleep
import functions as f
import renderer
import creatures
import sys

class rules():

	global snakeSymbol, snakeHeadSymbol, mouseSymbol, isEmpty, looping

	snakeSymbol = 'x'
	snakeHeadSymbol = 'X'
	mouseSymbol = 'Y'
	wallSymbol = '#'
	isEmpty = ' '
	looping = True

	'''
	This function reads keyboard input and checks if snake's head is on mouse.
	If snake's head is on mouse, then we use eat(), else we use move().
	'''
	def move_creature(catcher, food_for_catcher):
		insert = f.functions.getChar()
		global length

		# Lenght of Snake
		length = len(catcher.coordinates)

		if(insert=="w"):
			# If Snake's coordinates are in 1st line game is over
			if(catcher.coordinates[0][0] == 1):
				rules.gameOver()
			# If snake X and Y coordinates equals to mouse X and Y
			elif(catcher.coordinates[0][0] - 1 == food_for_catcher.coordinates[0][0] and catcher.coordinates[0][1] == food_for_catcher.coordinates[0][1]):
				rules.eat(mouseSymbol, sub, catcher, food_for_catcher)
				renderer.map.print_table()
			else:
				rules.move(mouseSymbol,sub, catcher)
				renderer.map.print_table()
		elif(insert=="s"):
			if(catcher.coordinates[0][0] == 10):
				rules.gameOver()
			elif(catcher.coordinates[0][0] + 1 == food_for_catcher.coordinates[0][0] and catcher.coordinates[0][1] == food_for_catcher.coordinates[0][1]):
				rules.eat(mouseSymbol, add, catcher, food_for_catcher)
				renderer.map.print_table()
			else:
				rules.move(mouseSymbol,add, catcher)
				renderer.map.print_table()
		elif(insert=="a"):
			if(catcher.coordinates[0][1] == 1):
				rules.gameOver()
			elif(catcher.coordinates[0][0] == food_for_catcher.coordinates[0][0] and catcher.coordinates[0][1] - 1 == food_for_catcher.coordinates[0][1]):
				rules.eat(snakeSymbol, sub, catcher, food_for_catcher)
				renderer.map.print_table()
			else:
				rules.move(snakeSymbol,sub,catcher)
				renderer.map.print_table()
		elif(insert=="d"):
			if(catcher.coordinates[0][1] == 10):
				rules.gameOver()
			elif(catcher.coordinates[0][0] == food_for_catcher.coordinates[0][0] and catcher.coordinates[0][1] + 1 == food_for_catcher.coordinates[0][1]):
				rules.eat(snakeSymbol, add, catcher, food_for_catcher)
				renderer.map.print_table()
			else:
				rules.move(snakeSymbol,add,catcher)
				renderer.map.print_table()
		print('SCORE:',(length-1))

	'''
	When mouse is catched this function increases snake's size, recalculates snake's coordinates and draw it on the map.
	It also draws new mouse on the map.
	'''
	def eat(axis, symbol, catcher, food_for_catcher):
		temp_y = catcher.coordinates[0][0]
		temp_x = catcher.coordinates[0][1]

		catcher.add_coordinate([food_for_catcher.coordinates[0][0],food_for_catcher.coordinates[0][1]])

		del food_for_catcher.coordinates[0]

		global length
		length+=1

		for x in range(0,length):
			if(x==(length-1)):
				break
			catcher.coordinates[length-1-x][0] = catcher.coordinates[length-2-x][0]
			catcher.coordinates[length-1-x][1] = catcher.coordinates[length-2-x][1]
			renderer.map.table[catcher.coordinates[length-1-x][0]][catcher.coordinates[length-1-x][1]] = snakeSymbol
			sleep(0.01)
		if(axis==snakeSymbol):
			catcher.coordinates[0][0] = temp_y
			catcher.coordinates[0][1] = f.functions.operation(temp_x, symbol, 1)
		elif(axis==mouseSymbol):
			catcher.coordinates[0][1] = temp_x
			catcher.coordinates[0][0] = f.functions.operation(temp_y, symbol, 1)
		renderer.map.table[catcher.coordinates[0][0]][catcher.coordinates[0][1]] = snakeHeadSymbol
		food_for_catcher.spawn(mouseSymbol)

	# If mouse is not catched this function recalculates new snake's coordinates and draw it on the map.
	def move(axis, symbol, catcher):
		temp_y = catcher.coordinates[0][0]
		temp_x = catcher.coordinates[0][1]
		renderer.map.table[catcher.coordinates[length-1][0]][catcher.coordinates[length-1][1]] = isEmpty
		for x in range(0,length):
			if(x==(length-1)):
				break
			catcher.coordinates[length-1-x][0] = catcher.coordinates[length-2-x][0]
			catcher.coordinates[length-1-x][1] = catcher.coordinates[length-2-x][1]
			renderer.map.table[catcher.coordinates[length-1-x][0]][catcher.coordinates[length-1-x][1]] = snakeSymbol
		if(axis==mouseSymbol):	
			catcher.coordinates[0][1] = temp_x
			catcher.coordinates[0][0] = f.functions.operation(temp_y, symbol, 1)
		elif(axis==snakeSymbol):
			catcher.coordinates[0][1] = f.functions.operation(temp_x, symbol, 1)
			catcher.coordinates[0][0] = temp_y
		renderer.map.table[catcher.coordinates[0][0]][catcher.coordinates[0][1]] = snakeHeadSymbol

	def exit():
		renderer.map.print_table()
		print('DO NOT LEAVE FIELD!')

	def gameOver():
		game_over = 'GAME OVER!\n'
		f.functions.write_text(game_over)
		sys.exit()