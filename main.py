from decompose import *
from rules import *

def main():

	print("hi im eliza how u")

	while(True):

		turn = input()
		d = decompose(turn)
		fragments = d[0]
		key = d[1]

		rule = get_rule(fragments, key)




main()