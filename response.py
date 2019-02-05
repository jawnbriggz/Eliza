from dictionary import *
from compare import *
from rules import *

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

def transform(responses, fragments):

#	TODO
#			start off here with the broken down rules and start to transform them into an actual answer

	print(responses)
	print(fragments)

	return(responses)
