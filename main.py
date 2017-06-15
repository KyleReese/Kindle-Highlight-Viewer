import sys, random
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

class Quote(object):

	def __init__(self):
		super(Quote, self).__init__()
		self.list = []
		self.index = 0
		self.filled = False

	def addFromFile(self, name):
		file = open(name, 'r', encoding="utf8")
		quoteNext = False
		with file:
			for line in file:
				if quoteNext == True:
					self.list.append(line)
					quoteNext = False
				elif line == "\n":
					quoteNext = True
		self.filled = True

	def getRandomQuote(self):
		return random.choice(self.list)

	def isFilled(self):
		return self.filled


class Window(QWidget):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle('Kindle Highlight Viewer')
		self.quotes = Quote()
		self.home()

	def home(self):
		self.grid = QGridLayout()
		self.grid.setSpacing(10)

		fileBtn = QPushButton('Open File', self)
		fileBtn.clicked.connect(self.file_open)

		self.textView = QTextEdit()
		self.textView.setReadOnly(True)
		self.textView.textCursor().insertHtml('Open your Kindle "My Clippings.txt" file')

		randomBtn = QPushButton('Random Quote', self)
		randomBtn.clicked.connect(self.randomQuote)

		self.grid.addWidget(fileBtn, 1, 0)
		self.grid.addWidget(randomBtn, 2, 0)
		self.grid.addWidget(self.textView, 3, 0)
		self.setLayout(self.grid)
		self.show()

	def file_open(self):
		# name is a tupple otherwise the app crashed
		name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
		self.quotes.addFromFile(name)

	def randomQuote(self):
		self.textView.clear()
		if self.quotes.isFilled():
			self.textView.textCursor().insertHtml(self.quotes.getRandomQuote())
		else:
			self.textView.textCursor().insertHtml('You need to load your Kindle "My Clippings.txt" file')

def run():
	app = QApplication(sys.argv)
	gui = Window()
	sys.exit(app.exec_())

run()