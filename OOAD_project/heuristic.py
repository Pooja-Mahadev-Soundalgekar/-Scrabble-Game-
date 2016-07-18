
import board, player, tile, aistats


class Heuristic(object):
	
	def __init__(self):
		self.stats = aistats.AIStats()

	def adjust(self, trayTiles = None, seedRatio = None, playTiles = None):
		return 0		


