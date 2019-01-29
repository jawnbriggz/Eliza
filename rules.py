
def get_rule(fragments, key):

	print(fragments)

	pattern = []
	for f in fragments:
		if(not f == "" and not f == " "):
			if(f == key):
				pattern.append(f)
			else:
				pattern.append(0)

	print(pattern)


