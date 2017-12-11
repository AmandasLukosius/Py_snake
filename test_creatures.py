import unittest
import renderer
from creatures import creature

class TestCreature(unittest.TestCase):

	def test_coordinates(self):
		Sheep = animal()

		Sheep.add_coordinate([5,6])

		self.assertEqual(Sheep.coordinates[0], [5,6])

		Sheep.add_coordinate([1,10])

		self.assertEqual(Sheep.coordinates[1], [1,10])

	def test_spawn(self):
		Elephant = animal()
		renderer.map.create_map()
		Elephant.spawn('E')

		assert Elephant.coordinates[0] is not None
		# Check X
		assert Elephant.coordinates[0][0] <= renderer.map.get_mapSize() - 2
		# Check Y
		assert Elephant.coordinates[0][1] <= renderer.map.get_mapSize() - 2

if __name__ == '__main__':
	unittest.main()