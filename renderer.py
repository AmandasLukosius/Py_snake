import colorama
from termcolor import colored
import rules as r

class map():

	map_size = 10
	table = []
	max_snake_length = (map_size - 2) * (map_size - 2)

	def create_map():
		for x in range(0, map.map_size):
			temp = []
			if(x==0 or x==map.map_size-1):
				# First and last lines
				for x in range(0, map.map_size):
					temp.append('#')
			else:
				# Middle lines
				for x in range(0, map.map_size):
					if(x==0 or x==map.map_size-1):
						temp.append('#')
					else:
						temp.append(' ')
			map.table.append(temp)

	def print_map():
		colorama.init()
		element_colors = {r.rules.wallSymbol: 'green', r.mouseSymbol: 'cyan', r.isEmpty: 'white', r.snakeHeadSymbol: 'red', r.snakeSymbol: 'white'}
		for x in map.table:
			k = " ".join(colored(element, element_colors[element]) for element in x)
			print(k)

	def get_mapSize():
		return map.map_size