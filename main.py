import gameStart, renderer, creatures
import rules as r
import functions as f
from time import sleep

game_over_message='GAME OVER!\n'
winning_message='Congratulations!!!\nYou won!\n'

gameStart.gameStart.greetings()

# Creating map
renderer.map.create_map()

# Creating instances of classes
Snake = creatures.creature()
Mouse = creatures.creature()

# Adding Snake and Mouse to the map
Snake.spawn(r.snakeHeadSymbol)
Mouse.spawn(r.mouseSymbol)

# Printing map
renderer.map.print_map()

# Looping snake's movement while it eats itself
while(r.looping):
	if(Snake.coordinates[0] in Snake.coordinates[1:]):
		f.functions.write_text(game_over_message)
		break
	if(len(Snake.coordinates) == renderer.map.max_snake_length):
		f.functions.write_text(winning_message)
		break
	r.rules.move_creature(Snake, Mouse)
	sleep(0.1)