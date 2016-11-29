from datetime import datetime
import os
import sys
import threading
import time

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
                for split in category.splits:
                    for splitTime in split.splitTimes:
                        print splitTime

class StoppableThread(threading.Thread):
	"""Thread class with a stop() method. The thread itself has to check
	regularly for the stopped() condition."""

	def __init__(self, group=None, target=None, name=None,
                     args=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
		self.target = target
		self.args = args
		self.kwargs = kwargs
		self._stop = threading.Event()

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()

	def run(self):
		while not self.stopped():
			self.target()
			time.sleep(.1)


class Timer(object):
	def __init__(self):
		self.category = None
		self.currentSplitIdx = -1
		self.currentSplitTime = None
                self.startTime = None

	def startTimer(self, category):
		self.category = category
		self.currentSplitIdx = -1
		self.next()

	def next(self):
		self.currentSplitIdx += 1
                now = datetime.now()

                if self.currentSplitIdx == 0:
                    self.startTime = now

		# Skip this on first call
		if self.currentSplitIdx > 0:
			self.currentSplitTime.timeEnd = now

		# Skips this on last call
		if self.currentSplitIdx < len(self.category.splits):
			self.currentSplitTime = SplitTime()
			self.currentSplitTime.timeStart = datetime.now()

			currentSplit = self.category.splits[self.currentSplitIdx]
			currentSplit.splitTimes.append(self.currentSplitTime)

			self.waitForNextSplit()


	def waitForNextSplit(self):
		self.timerRunning = True
		t = StoppableThread(target=self.showTimer)
		t.start()
		#os.system("pause")
                os.system('read -s -n 1')
		t.stop()
                print

		self.next()

	def showTimer(self):
		sys.stdout.write("\r")
                currentSplit = self.category.splits[self.currentSplitIdx]
		sys.stdout.write(str(currentSplit) + "\t\t" 
                                 + str(datetime.now() - self.startTime))
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
		self.timeStart = None
		self.timeEnd = None

	def __str__(self):

		return (str(self.timeStart.date()) + "\n"
                        + "\t" + str(self.timeStart.time()) + " - " 
                               + str(self.timeEnd.time()) + " : "
			+ "\t" + str(self.timeEnd - self.timeStart))
