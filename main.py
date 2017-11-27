import gameStart, renderer, creatures
import rules as r
import functions as f
from time import sleep

game_over='GAME OVER!\n'

gameStart.gameStart.greetings()

# Creating instances of classes
Snake = creatures.creature()
Mouse = creatures.creature()

# Adding Snake and Mouse to the map
Snake.spawn(r.snakeHeadSymbol)
Mouse.spawn(r.mouseSymbol)

# Printing map
renderer.map.print_table()

# Looping snake's movement while it eats itself
while(r.looping):
	r.rules.move_creature(Snake, Mouse)
	if(Snake.coordinates[0] in Snake.coordinates[1:]):
		r.looping = False
		f.functions.write_text(game_over)
	sleep(0.1)