class Model(object):
	def __init__(self):
		self.dataManager = DataManager()
		self.games = self.dataManager.getGamesData()




class DataManager(object):
	def __init__(self):
		pass

	def getGamesData(self):
		game = Game('game1')
		category = Category('cat1')
		game.categories.append(category)
		games = [game]
		return games


class Game(object):
	def __init__(self, name):
		self.name = name
		self.categories = []

	def __str__(self):
		return self.name


class Category(object):
	def __init__(self, name):
		self.name = name
		self.splits = []
		
	def __str__(self):
		return self.name


class Split(object):
	def __init__(self, name):
		self.name = name
		self.splitTimes = []


class SplitTime(object):
	def __init__(self):
		self.date = None
		self.timeStart = None
		self.timeEnd = None
