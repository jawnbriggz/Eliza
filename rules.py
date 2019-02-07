
def get_rule(fragments, key):

	place = 0

	pattern = []
	for f in fragments:
		if(not f == "" and not f == " "):
			if(f in key):
				pattern.append(f)
			else:
				pattern.append(place)
				place = place + 1

	return(pattern)


