from nose.tools import *
from ex48 import parser

def test_sentence():
	s1 = parser.Sentence(("noun", "bear"), ("verb", "run"), ("noun", "south"))
	assert_equal(s1.subject, "bear")
	assert_equal(s1.verb,    "run")
	assert_equal(s1.object,  "south")
	s2 = parser.Sentence(("noun", "player"), ("noun", "kill"), ("noun", "bear"))
	assert_equal(s2.subject, "player")
	assert_equal(s2.verb,    "kill")
	assert_equal(s2.object,  "bear")

def test_peek():
	words_list = [("noun", "bear"), ("verb", "run"), ("noun", "south")]
	words_list_copy = words_list[:]
	for word in words_list_copy:
		assert_equal(parser.peek(words_list), word[0])
		words_list.pop(0)

	assert_equal(parser.peek(words_list), None)

def test_match():
	words_list = [("noun", "player"), ("noun", "kill"), ("noun", "bear")]
	words_list_copy = words_list[:]
	for word in words_list_copy:
		assert_equal(parser.match(words_list, word[0]), word)
		assert_not_in(word, words_list)

def test_skip():
	words_list = [("stop", "A"), ("noun", "player"), ("noun", "kill"), ("stop", "the"),("noun", "bear")]
	parser.skip(words_list, "stop")
	assert_not_in(("stop", "A"), words_list)
	words_list = words_list[2:]
	parser.skip(words_list, "stop")
	assert_not_in(("stop", "the"), words_list)

def test_parse_verb():
	pass

def test_parse_object():
	pass

def test_parse_subject():
	pass

def test_parse_sentence():
	pass
