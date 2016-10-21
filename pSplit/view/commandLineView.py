class CommandLineView(object):
	def __init__(self, controller):
		self.controller = controller

	def show(self):
		self.showMainMenu()


	def showMainMenu(self):
		while True:
			command = raw_input("Enter Main Menu Command: ")

			result = self.parseMainMenuCommand(command)

			if result == "gameSelected":
				self.showGameMenu()


	def showGameMenu(self):
		while True:
			command = raw_input("Enter Game Command: ")

			result = self.parseGameMenuCommand(command)

			if result == "categorySelected":
				self.showCategoryMenu()


	def showCategoryMenu(self):
		while True:
			command = raw_input("Enter Category Command: ")

			result = self.parseCategoryMenuCommand(command)

			if result == "categorySelected":
				self.showCategoryMenu()


	def parseMainMenuCommand(self, command):
		if command == "l":
			self.listGames()
		elif command == "s":
			self.selectGame()
			if self.selectedGame is not None:
				return "gameSelected"

	def parseGameMenuCommand(self, command):
		if command == "l":
			self.listCategories(self.selectedGame)
		elif command == "s":
			self.selectCategory(self.selectedGame)
			if self.selectedCategory is not None:
				return "categorySelected"

	def parseCategoryMenuCommand(self, command):
		if command == "l":
			self.listSplits(self.selectedCategory)
		elif command == "a":
			self.addSplit(self.selectedCategory)
		elif command == "d":
			self.deleteSplit(self.selectedCategory)
		elif command == "r":
			self.renameSplit(self.selectedCategory)
		elif command == "m":
			self.moveSplit(self.selectedCategory)
		elif command == "s":
			self.selectSplit(self.selectedCategory)
			if self.selectedSplit is not None:
				return "splitSelected"
		elif command == "g":
			self.startCategoryTimer(self.selectedCategory)





	def listObjectIndices(self, objects):
		for idx, o in enumerate(objects):
			print idx, "-", o

	def selectObjectIndex(self, objects):
		o = None

		self.listObjectIndices(objects)

		while True:
			idx = raw_input("Select Index: ")
			if idx == "q":
				break
			try:
				idx = int(idx)
				o = objects[idx]
				print "Selected ", o
				break

			except IndexError:
				print "Select a valid index!"
			except TypeError:
				print "Select a valid index!"
			except ValueError:
				print "Select a valid index!"

		return o


	def listGames(self):
		games = self.controller.getGames()
		self.listObjectIndices(games)

	def selectGame(self):
		games = self.controller.getGames()
		self.selectedGame = self.selectObjectIndex(games)


	def listCategories(self, game):
		categories = self.controller.getCategories(game)
		self.listObjectIndices(categories)

	def selectCategory(self, game):
		categories = self.controller.getCategories(game)
		self.selectedCategory = self.selectObjectIndex(categories)

