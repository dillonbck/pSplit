#!/usr/bin/python2

import sys
from os import path
sys.path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))

from pSplit.controller.controller import Controller


def start():
	controller = Controller()
	controller.run()

if __name__ == "__main__":
	start()
	
