from dictionary import *

def compare_fragments(rule1, rule2):

	same = True

	idx = 0
	for t in rule1:
		if(len(rule2) >= len(rule1)):
			print("compare ", t)
			print("and ", rule2[idx])
			if(t == rule2[idx] or (isinstance(t, int) and isinstance(rule2[idx], int))):
				idx += 1
				continue
			else:
				return False
		else:
			return(False)

	return same
