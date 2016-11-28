from datetime import datetime
import os
import sys
from threading import Thread

class Model(object):
	def __init__(self):
		self.dataManager = DataManager()
		self.games = self.dataManager.getGamesData()
		self.timer = Timer()

	def addGame(self, gameName):
		newGame = Game(gameName)
		self.model.games.append(newGame)

	def addGameCategory(self, game, categoryName):
		newCategory = Category(categoryName)
		game.categories.append(newCategory)

	def addCategorySplit(self, category, splitName):
		newSplit = Split(splitName)
		category.splits.append(newSplit)


	def startTimer(self, category):
		self.timer.startTimer(category)


class Timer(object):
	def __init__(self):
		self.category = None
		self.currentSplitIdx = -1
		self.currentSplitTime = None

	def startTimer(self, category):
		self.category = category
		self.currentSplitIdx = -1
		self.next()

	def next(self):
		self.currentSplitIdx += 1

		# Skip this on first call
		if self.currentSplitIdx > 0:
			self.currentSplitTime.timeEnd = datetime.now()

		# Skips this on last call
		if self.currentSplitIdx < len(self.category.splits):
			self.currentSplitTime = SplitTime()
			self.currentSplitTime.timeStart = datetime.now()

			currentSplit = self.category.splits[self.currentSplitIdx]
			currentSplit.splitTimes.append(self.currentSplitTime)

			self.waitForNextSplit()


	def waitForNextSplit(self):
		self.timerRunning = True
		t = Thread(target=self.showTimer)
		t.start()
		os.system("pause")
		self.timerRunning = False

		self.next()



	def showTimer(self):
		while self.timerRunning:
		    sys.stdout.write("\r")
		    sys.stdout.write(str(datetime.now().microsecond))
		    sys.stdout.flush()



class DataManager(object):
	def __init__(self):
		pass

	def getGamesData(self):
		game = Game('Dustforce')
		category = Category('Forest Only SS')
		game.categories.append(category)
		splits = [Split("First"), Split("Second"), Split("Third"), 
				  Split("Fourth")]
		category.splits += splits
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

	def __str__(self):
		return self.name


class SplitTime(object):
	def __init__(self):
		self.date = None
		self.timeStart = None
		self.timeEnd = None

	def __str__(self):

		return (str(date) + "\n"
			    + "\t" + str(self.timeStart) + " - " + str(self.timeEnd) + " : "
			    + "\t" + str(self.timeEnd - self.timeStart))
