import colorama
from termcolor import colored
import rules as r

class map():
	table = [	['#','#','#','#','#','#','#','#','#','#','#','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
				['#','#','#','#','#','#','#','#','#','#','#','#']]

	def print_table():
		colorama.init()
		element_colors = {r.rules.wallSymbol: 'green', r.mouseSymbol: 'cyan', r.isEmpty: 'white', r.snakeHeadSymbol: 'red', r.snakeSymbol: 'white'}
		for x in map.table:
			k = " ".join(colored(element, element_colors[element]) for element in x)
			print(k)