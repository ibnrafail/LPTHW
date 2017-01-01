class ParserError(Exception):
	pass


class Sentence(object):

	def __init__(self, subject, verb, obj):
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]


def peek(word_list):
	"""
	Peeks at a list of words and returns
	what type of word it is
	"""
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None


def match(word_list, expected_type):
	"""
	confirms that the expected word
	is the right type, takes it off the list,
	and returns the word.
	"""
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expected_type:
			return word
		else:
			return None
	else:
		return None


def skip(word_list, word_type):
	"""
	Skips all words of word_type
	in sequence in the word_list
	"""
	while peek(word_list) == word_type:
		match(word_list, word_type)


def parse_verb(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParseError("Expected a verb next.")


def parse_object(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParseError("Expected a noun or direction next.")


def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)
