import dictionarywords, math

class WordFrequency:
	
	FILENAME = "media/wordfreq.txt"
	DICTIONARY = "media/scrabblewords_usage.txt"
	
	def __init__(self):
		
		self.count = {}
		self.load()
		self.dict = dictionarywords.DictionaryWords(WordFrequency.DICTIONARY)
		
	def load(self):
		try:
			freqFile = open(WordFrequency.FILENAME, 'r')
		
			for line in freqFile:
				tokens = line.split()
				assert len(tokens) == 2
				word = tokens[0]
				freq = int(tokens[1])
			
				self.count[word] = freq
		except IOError as e:
			pass
			
	def save(self):
		
		freqFile = open(WordFrequency.FILENAME, 'w')
		
		for word in self.count.keys():
			freqFile.write(word+" "+str(self.count[word])+"\n")
			
	def wordPlayed(self, word):
		if self.count.has_key(word):
			self.count[word] += 1
		else:
			self.count[word] = 1
