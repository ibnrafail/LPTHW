"""Lexicon module"""

dirs  = ("north", "south", "east",
		 "west", "down", "up",
		 "left", "right", "back")
verbs = ("go", "stop", "kill", "eat")
stops = ("the", "in", "of", "from", "at", "it")
nouns = ("door", "bear", "princess", "cabinet")


def scan(user_input):
	"""A scanner function, takes a string of raw input
	   from a user and returns a sentence that's composed
	   of a list of tuples with the (TOKEN, WORD) pairings."""

	res_sentence = list()
	words = user_input.split()

	for word in words:
		if word.isdigit():
			res_sentence.append(("number", int(word)))
			continue
		elif word in dirs:
			res_sentence.append(("direction", word.lower()))
			continue
		elif word in verbs:
			res_sentence.append(("verb", word.lower()))
			continue
		elif word in stops:
			res_sentence.append(("stop", word.lower()))
			continue
		elif word in nouns:
			res_sentence.append(("noun", word.lower()))
			continue
		else:
			res_sentence.append(("error", word))

	return res_sentence
