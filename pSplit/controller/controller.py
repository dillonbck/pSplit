from pSplit.model.model import Model
from pSplit.view.commandLineView import CommandLineView

class Controller(object):
	def __init__(self):
		self.model = Model()
		self.view = CommandLineView(self)

	def run(self):
		self.view.show()


	def setTimeSplit(self):
		pass

	def undoLastTimeSplit(self):
		pass

	def startTime(self):
		pass

	def pauseTime(self):
		pass




	def addGame(self, name):
		pass

	def addGameCategory(self, game, name):
		pass

	def addCategorySplit(self, category, name):
		pass


	def getGames(self):
		games = self.model.games
		return games

	def getCategories(self, game):
		categories = game.categories
		return categories