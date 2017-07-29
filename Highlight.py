class Highlight(object):
	def __init__(self):
		super(Highlight, self).__init__()
		self.title = ''
		self.author = ''
		self.text = ''
		self.pageNum = 0
		self.loc = 0
		self.dateAdded = ''

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
			authorIndex = entry[0].rfind('(')
			highlight.title = entry[0][:authorIndex]
			highlight.author = entry[0][authorIndex:]
			highlight.pageNum, highlight.loc, highlight.dateAdded = entry[1].split('|')
			highlight.text = entry[2]
			yield highlight

