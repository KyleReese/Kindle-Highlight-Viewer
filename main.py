import sys, random
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog

class Quote(object):

	def __init__(self):
		super(Quote, self).__init__()
		self.list = []
		self.index = 0

	def addItem(self, item):
		self.list.append(item)

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

	def getRandomQuote(self):
		return random.choice(self.list)


class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle('Open File')
		self.quotes = Quote()
		self.home()

	def home(self):
		btn = QPushButton('Open File', self)
		btn.clicked.connect(self.file_open)

		btn.resize(btn.sizeHint())  #set to acceptable size automatic
		btn.move(0, 0)
		self.show()

	def close_application(self):
		print('whooo so custom')
		sys.exit()
		
	def file_open(self):
		# need to make name an tupple otherwise i had an error and app crashed
		name, _ = QFileDialog.getOpenFileName(self, 'Open File', options=QFileDialog.DontUseNativeDialog)
		self.quotes.addFromFile(name)
		print(self.quotes.getRandomQuote())


def run():
	app = QApplication(sys.argv)
	Gui = Window()
	sys.exit(app.exec_())

run()