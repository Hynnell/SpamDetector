import numpy as np

from extract import *

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
	final_words_train = count_words(training)
	# final_words_train = remove_stop_words(counted_train)
	train_x = extract_features(training, final_words_train)

	# Read data from testing
	final_words_test = count_words(testing)
	# final_words_test = remove_stop_words(counted_test)
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
