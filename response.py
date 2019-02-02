from dictionary import *
from compare import *

def get_response(rule, key):

	n = len(key)
	print("KEY ", key)
	response_rules = []
	for i in range(0,n):
		temp = key[i]
		response_rules = keywords[temp]


	print("response_rules : ", response_rules)

	print("KEY ", key)

	rules = response_rules[0]

	print("heckin rules", rules)

	print("r in rules: ")

	response_strings = rules[1]

	return(response_strings)