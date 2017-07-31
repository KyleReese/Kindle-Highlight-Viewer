import sys, random
from Highlight import Highlight, Quote
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication

def parseHighlight(filename):
	with open(filename, 'r',encoding='utf8') as infile:
		line = ''
		while True:
			while not line.startswith('=========='): 
				line = next(infile) 
				continue  

			entry = []
			for line in infile:
				line = line.strip()
				if line.startswith('=========='): break
				if line:
					entry.append(line)

			highlight = Highlight()
			try:
				authorIndex = entry[0].rfind('(')
				highlight.title = entry[0][:authorIndex]
				highlight.author = entry[0][authorIndex:]
			except: pass
			try:
				highlight.pageNum, highlight.loc, highlight.dateAdded = entry[1].split('|')
			except:	pass
			try:
				highlight.text = entry[2]
			#If there is no highlight text break out of generator without yielding to stop iterating loop
			except: break
			yield highlight

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
		# name is a tupple to prevent crash
		name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
		for highlight in parseHighlight(name):
			self.quotes.addQuote(highlight)
		self.randomQuote()
		# self.quotes.addFromFile(name)

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