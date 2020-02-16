from collections import Counter
import os
import numpy as np

# Helper function which counts the frequency of each word in a directory.
def count_words(directory):
	emails = [os.path.join(directory,file) for file in os.listdir(directory)] 
	track_words = []
	for email in emails:
		with open(email, encoding="latin-1") as email:
			for line in email:
				words = line.split() # Create list of words on a line
				track_words += words # Add each word to total count

	count_words = Counter(track_words) # Count frequency of each word
	# print(count_words)
	return count_words

#Helper function which removes "stop words" and returns a list of the most common.
def remove_stop_words(counted):
	words = list(counted.keys())

	for elem in words:
		if len(elem) == 1 or len(elem) == 2: # Remove stop words.
			del counted[elem]
		if elem.isalpha() == False: # Remove non-alphabetical words.
			del counted[elem]

	counted = counted.most_common(3000) # Take the most common 3000 words
	# print(counted)
	return counted

def extract_features(directory, dictionary):
	files = [os.path.join(directory,file) for file in os.listdir(directory)]

	# Create the matrix to store the features
	features_matrix = np.zeros((len(files), 3000))
	# print(features_matrix)

	docID = 0
	# traceback = [] #This is used to correlate words for the feedback

	for emails in files:
		with open(emails, encoding="latin-1") as email:
			for line in email:
				words = line.split() # Create list of words on a line
				for word in words:
					wordID = 0
					for i,d in enumerate(dictionary): # Here i is the index and d is the word
						if d[0] == word: # d[0] is the word, d[1] is the frequency.
							wordID = i
							# traceback[i] = d[0]
							features_matrix[docID, wordID] = 1 # Set the occurrence of that word.
							# features_matrix[docID, wordID] = word.count(word) # Original sets the frequency

			docID += 1 #Increment the index to indicate which email we are at.

	return features_matrix


# Distance between instances x1 and x2
def dist(x1, x2):
  # TODO: YOUR CODE HERE
  dist = np.linalg.norm(x1-x2)
  dist = dist**2
  return dist


def classify(train_x, train_y, k, x):
	'''
	Use distance to determine k nearest x vectors, and then use sum on
	corresponding y values. 

	train_x : list of vectors
	train_y : vector of classifications
	x : vector we use to compare to other vectors within train_x
	'''

	length_train = len(train_x)
	dists = list()

	for i in range(len(train_x)):
		distance = dist(x, train_x[i])
		dists.append(distance)

	index_nearest = np.argpartition(dists, k)[:k]

	classification_sum = 0
	k_near = list()
	for elem in index_nearest:
		classification_sum += train_y[elem]

	if classification_sum >= 0:
		return 1
	elif classification_sum < 0:
		return -1


# Function to compare results of classify with expected outcome to compute accuracy
def runTest(test_x, test_y, train_x, train_y, k):
	correct = 0
	for (x,y) in zip(test_x, test_y):
		if classify(train_x, train_y, k, x) == y: # Compare call to classify with test_y
			correct += 1
	acc = float(correct)/len(test_x)
	return acc



def main():

	# File Paths
	training = "./data/lingspam_public/bare/part1"
	testing = "./data/lingspam_public/bare/part2"

	# Read data from training
	counted_train = count_words(training)
	final_words_train = remove_stop_words(counted_train)
	train_x = extract_features(training, final_words_train)

	# Read data from testing
	counted_test = count_words(testing)
	final_words_test = remove_stop_words(counted_test)
	test_x = extract_features(testing, final_words_test)

	# Creating our labels, 1 indicates spam, -1 indicates ham
	train_y = np.zeros(289)
	train_y[0:240] = -1
	train_y[241:288] = 1

	# Creating our labels, 1 indicates spam, -1 indicates ham
	test_y = np.zeros(289)
	test_y[0:240] = -1
	test_y[241:288] = 1

	k = 10
	acc = runTest(test_x, test_y, train_x, train_y, k)
	print("Accuracy:", acc)


if __name__ == '__main__':
	main()
