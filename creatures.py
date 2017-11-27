from random import randint
from time import sleep
import renderer

class creature():

	def __init__(self):
		self.coordinates = []

	def add_coordinate(self, coordinate):
		self.coordinates.append(coordinate)

	def spawn(self, mark):
		looping = True
		while(looping):
			y = randint(1,10)
			x = randint(1,10)
			if renderer.map.table[y][x] == ' ':
				renderer.map.table[y][x] = mark
				self.add_coordinate([y,x])
				looping = False
			sleep(0.001)