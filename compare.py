from dictionary import *

def compare_fragments(rule, key):

	places = [0,1,2,3,4,5,6,7,8,9]

	same = True

	key_idx = 0
	for t in rule:
		if(t in places or t in key):
			print("good so far: ", t)
		else:
			same = False

	return same
