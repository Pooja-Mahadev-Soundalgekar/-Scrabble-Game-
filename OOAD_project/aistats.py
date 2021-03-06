
import pygame, random, sys, time, math, dictionarywords
from pygame.locals import *

class AIStats():
	
	FILENAME = "media/aistats.txt"  
	COLLECT_WORD_DATA = False		
	COLLECT_GAME_DATA = False		
	def __init__(self):
		
		self.timingInfo = []
		self.letterPlays = {}
		for code in range(ord('A'), ord('Z')+1):
			char = chr(code)
			self.letterPlays[char] = []
		
		self.letterPlays["_"] = []
		self.scores = []
		
		self.seedRatio = []
		
		self.load()
	

	def load(self):
		try:
			statsFile = open(AIStats.FILENAME, 'r')
			
			MODE = "none"
			for line in statsFile:
				
				if line != "\n":
					line = line.rstrip()
					if MODE == "TIMING:":
						tokens = line.split()
					
						assert len(tokens) == 2
						self.timingInfo.append((float(tokens[0]) , float(tokens[1])))
					
					elif MODE == "LETTERS:":
						tokens = line.split()

						assert len(tokens) == 2
						self.letterPlays[tokens[0]].append(float(tokens[1]))
						
					elif MODE == "SEED:":
						tokens = line.split()

						assert len(tokens) == 3
						self.seedRatio.append((int(tokens[0]), int(tokens[1]), float(tokens[2])))						
						
					elif MODE == "GAME:":
						tokens = line.split()
						self.scores.append([int(token) for token in tokens])
						
						

				else:
					MODE = "none"
								
				if line == "TIMING:":
					MODE = "TIMING:"
				elif line == "LETTERS:":
					MODE = "LETTERS:"
				elif line == "SEED:":
					MODE = "SEED:"
				elif line == "GAME:":
					MODE = "GAME:"
					
		except IOError as e:
			pass

	def save(self):
		statsFile = open(AIStats.FILENAME, 'w')
		
		statsFile.write("TIMING:\n")
		for timeStamp in self.timingInfo:
			statsFile.write(str(timeStamp[0])+" "+str(timeStamp[1])+"\n")
		statsFile.write("\n")
			
		statsFile.write("LETTERS:\n")
		for code in range(ord('A'), ord('Z')+1):
			char = chr(code)
			if len(self.letterPlays[char]) > 0:
				for play in self.letterPlays[char]:
					statsFile.write(char+" "+str(play)+"\n")
		if len(self.letterPlays["_"]) > 0:
			for play in self.letterPlays["_"]:
				statsFile.write("_ "+str(play)+"\n")
		statsFile.write("\n")	
		
		statsFile.write("SEED:\n")
		for seeds in self.seedRatio:
			statsFile.write(str(seeds[0])+" "+str(seeds[1])+" "+str(seeds[2])+"\n")
		statsFile.write("\n")
		
		statsFile.write("GAME:\n")
		for game in self.scores:
			for score in game:
				statsFile.write(str(score)+" ")
			statsFile.write("\n")
		statsFile.write("\n")		
		
			
	def updateTiming(self, totalTime, timeAtMaxWord):
		if AIStats.COLLECT_WORD_DATA:
			self.timingInfo.append((totalTime, timeAtMaxWord))
		
	def updateLetterPlays(self, lettersUsed, points):
		if AIStats.COLLECT_WORD_DATA:
			for letter in lettersUsed:
				self.letterPlays[letter].append(points)
				
	def updateSeedRatio(self, (numSeeds, numTiles), points):
		if AIStats.COLLECT_WORD_DATA:
			self.seedRatio.append((numSeeds, numTiles, points))
				
	def saveGame(self, gameScores):
		if AIStats.COLLECT_GAME_DATA:
			self.scores.append(gameScores)

