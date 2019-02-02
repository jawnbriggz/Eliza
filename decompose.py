from dictionary import *

def decompose(turn):

	frags = turn.split(" ")

	# FIND THE KEYWORD
	key = []
	for w in frags:
		if(w in keywords):
			key.append(w)

	# CREATE PATTERN OUT OF FRAGMENTS
	pattern = []
	segment = ""
	for token in frags:
		if(token in key):
			if(len(segment) > 0):
				pattern.append(segment)
			pattern.append(token)
			segment = ""
		else:
			segment += token
			segment += " "
	pattern.append(segment)

	return pattern, key


