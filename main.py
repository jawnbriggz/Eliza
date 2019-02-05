from decompose import *
from rules import *
from compare import *
from response import *

def main():

	print("hi im eliza how u")

	while(True):

		turn = input()
		d = decompose(turn)
		fragments = d[0]
		key = d[1]

		rule = get_rule(fragments, key)
		responses = get_response(rule, key)

#		now that you have the possible response strings, use them plus "fragments" to transform and construct a ELIZA's response
#		print(responses)

#		respond back
		answer = transform(responses, fragments)
#		print(answer)





main()