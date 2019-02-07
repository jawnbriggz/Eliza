from dictionary import *
from compare import *
from rules import *
import re
import random

def get_response(rule, key):

	rules_set = False

	# get list of possible responses according to keyword
	# WORK ON CHOOSING BY PRIORITY
	n = len(key)
	response_rules = []
	for i in range(0,n):
		# THIS IS BY FIRST COME FIRST SERVE LOGIC NOT BY IMPORTANCE OF KEYWORD 
		if(not rules_set):
			temp = key[i]
			response_rules = keywords[temp]
			rules_set = True

	# list of records from the dictionary where key="[keyword]" and value="hey, this is a 3 string"
	m = len(response_rules)
	match = []
	for i in range(0,m):
		temp = response_rules[i]
		r = temp[0]
		#find the right rule pattern
		if(compare_fragments(rule, r)):
			match = match + temp[1]

	return(match)

def transform(fragments, rule):
#	start off here with the broken down rules and start to transform them into an actual answer
#	DONT  NEED responses IN THIS VERSION
#	print("responses: ", responses)
#	print("fragments", fragments)
#	print("rule: ", rule)

#	turn fragments list into a string so you can regex it to get the proper rules
	strang = ""
	for t in fragments:
		strang += t + " "

	rule_numbers = parse(strang)	
	idx = 0
	n = len(fragments)
	for i in range(0,n):
		if(fragments[i] in keywords):
			fragments[i] = change(fragments[i])
		else:
			if(idx == 0):
				fragments[i] = process(rule_numbers[i])
			else:
				idx += 1
				continue
		idx += 1

#	turn these frags back to strings
	repons = ""
	for thing in fragments:
		repons += thing + " "

#	DO SOME OTHER STUFF TO THE FRAGMENTS
	fin = repons.replace("ing", "")

	return(fin)


#parse and return logic
def parse(turn):

	rules = []

#	variables for regex search
	you_are = re.findall(r".*you.are.*", turn)
	offended = re.findall(r"(fuck|shit|poop|ass|bitch|suck|hate|stupid)", turn)
	you_me = re.findall(r".*you.*me.*", turn)
	eliza = re.findall(r"you", turn)

	mother = re.findall(r"(mother|mom|ma)", turn)
	brother = re.findall(r"brother", turn)
	father = re.findall(r"(father|dad|da|pa)", turn)
	sister = re.findall(r"sister", turn)

	question = re.findall(r"(wh.*\?|.*wh.*|wh.*)", turn)
	i_know = re.findall(r".*i.*know.*", turn)
	get_answer = re.findall(r"(yes|no|yeah|sure|nah|ya|maybe)", turn)
	dont = re.findall(r"dont", turn)
	to_be = re.findall(r"(be|am|are|is|being)", turn)

	emotion = re.findall(r"(sad|mad|angry|happy|bored|elated|joyful|excited)", turn)

	if(len(offended) > 0):
		rules.append(1)
	elif(len(you_me) > 0):
		rules.append(3)
	elif(len(emotion) > 0):
		rules.append(12)
	elif(len(eliza) > 0):
		rules.append(2)
	elif(len(you_are) > 0):
		rules.append(4)
	elif(len(mother) > 0):
		rules.append(8)
	elif(len(brother) > 0):
		rules.append(9)
	elif(len(father) > 0):
		rules.append(10)
	elif(len(sister) > 0):
		rules.append(11)	
	elif(len(question) > 0):
		rules.append(4)
	elif(len(i_know) > 0):
		rules.append(5)
	elif(len(get_answer) > 0):
		rules.append(6)
	elif(len(dont) > 0):
		rules.append(7)		
	else:
		rules.append(0)

	return rules


def process(logic):

	if(logic == 0):
		rando = random.randint(1,4)
		if(rando == 1):
			return "haha you're cute <3"
		elif(rando == 2):
			return "thats bogus"
		elif(rando == 3):
			return "ain't no thang"
		else:
			return "lol so random"
	elif(logic == 1):
		return "no need to be nasty"
	elif(logic == 2):
		return "I feel the same"
	elif(logic == 3):
		return "What makes you think"
	elif(logic == 4):
		return "I dont know why dont you www.google.com it..."
	elif(logic == 5):
		return "you think youre so smart?"
	elif(logic == 6):
		return "huh..."
	elif(logic == 7):
		return "what a shame"
	elif(logic == 8):
		return "dont you talk about my mother"
	elif(logic == 9):
		return "its interesting to know he"
	elif(logic == 10):
		return "tell me more about your father"
	elif(logic == 11):
		return "im interested to know more about"
	elif(logic == 12):
		return "why"
	else:
		return "hi bitch, bye bitch"


def change(word):

	if(word in trans):
		new_word = trans[word]
		word = new_word

	return word
