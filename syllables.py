'''
from nltk.corpus import cmudict
d = cmudict.dict()
import string

def nsyl(word):
	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

def is_haiku(text):
	poem = text.split()
	#poem = [s.translate(string.maketrans("",""), string.punctuation) for s in poem]
	syllables = [sum(nsyl(word)) for word in poem]
	print poem, syllables, sum(syllables)
	if sum(syllables) == 17:
		return True
	else:
		return False

if __name__ == "__main__":
	print is_haiku('An old silent pond... A frog jumps into the pond, splash! Silence again.')
'''