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

	def startCategoryTimer(self, category):
		self.model.startTimer(category)

	def pauseCategoryTimer(self, category):
		pass




	def addGame(self, gameName):
		self.model.addGame(gameName)

	def addGameCategory(self, game, categoryName):
		self.model.addGameCategory(game, categoryName)

	def addCategorySplit(self, category, splitName):
		self.model.addCategorySplit(category, splitName)


	def getGames(self):
		games = self.model.games
		return games

	def getCategories(self, game):
		categories = game.categories
		return categories

	def getSplits(self, category):
		splits = category.splits
		return splits
