import sys


GAME_TAGS = ["game", "gameplay", "let's play", "indie horror game", "horror game",
	"full gameplay", "full game", "walkthrough", "ending", "full game ending", 
	"itchio", "itchio game", "itchio horror game"]

DESCRIPTOR_TAGS = ["game"]


if len(sys.argv) != 3:
	print("Invalid command line arguments.")
	print("Usage: python3 tags.py <GAME TITLE> <DESCRIPTOR>")
	exit()

game = sys.argv[1]
descriptor = sys.argv[2]

output = []

output.append(game)

for str in GAME_TAGS:
	output_tag = game + " " + str
	output.append(output_tag)

output.append(descriptor)

for str in DESCRIPTOR_TAGS:
	output_tag = descriptor + " " str
	output.append(output_tag)

print(output)