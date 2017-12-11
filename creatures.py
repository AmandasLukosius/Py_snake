from random import randint
from time import sleep
import renderer, rules

class creature():

	def __init__(self):
		self.coordinates = []

	def add_coordinate(self, coordinate):
		self.coordinates.append(coordinate)

	def spawn(self, mark):
		looping = True
		while(looping):
			x = randint(1,renderer.map.get_mapSize() - 2)
			y = randint(1,renderer.map.get_mapSize() - 2)
			if renderer.map.table[x][y] == rules.isEmpty:
				renderer.map.table[x][y] = mark
				self.add_coordinate([x,y])
				looping = False
			sleep(0.001)