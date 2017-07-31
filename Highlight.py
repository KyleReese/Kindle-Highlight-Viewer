import random
class Highlight(object):
	def __init__(self):
		super(Highlight, self).__init__()
		self.title = ''
		self.author = ''
		self.text = ''
		self.pageNum = ''
		self.loc = ''
		self.dateAdded = ''

class Quote(object):

	def __init__(self):
		super(Quote, self).__init__()
		self.list = []
		self.index = 0
		self.filled = False

	# def addFromFile(self, name):
	# 	file = open(name, 'r', encoding="utf8")
	# 	quoteNext = False
	# 	with file:
	# 		for line in file:
	# 			if quoteNext == True:
	# 				self.list.append(line)
	# 				quoteNext = False
	# 			elif line == "\n":
	# 				quoteNext = True
	# 	self.filled = True

	def getRandomQuote(self):
		return random.choice(self.list).text

	def isFilled(self):
		return self.filled

	def addQuote(self, highlight):
		self.list.append(highlight)
		self.filled = True

