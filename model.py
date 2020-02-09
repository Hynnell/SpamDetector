from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

def feature_extraction(email):
	track_words = []
	with open(email) as email:
		for line in email:
			words = line.split()
			track_words += words

	count_words = Counter(track_words)
	
	# Remove unwanted features (meaningless words, non-alphabetic characters...)
	words = count_words.keys()
	for elem in words:
		if len(elem) == 1 or len(elem) == 2:
			del count_words[elem]
		if elem.isalpha() == False:
			del count_words[elem]
			
	print(count_words)
	return count_words

def main():
	# Test Email

	text = "./data/enron1/spam/0006.2003-12-18.GP.spam.txt"
	feature_extraction(text)



if __name__ == '__main__':
	main()