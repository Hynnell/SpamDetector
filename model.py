from collections import Counter
import os
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

from extract import *

'''
TODO: 

- Verify feature extraction works
- Test on sample data (currently takes a very long time to run)
- Refine text
- Connect to GUI
- Train the app so it doesnt need to be trained each time. 
- Support single email submission
'''


'''
Notes about the confusion matrix: 
In binary classification, the count of:
true negatives is C[0,0] <- want this high
false negatives is C[1,0]
true positives is C[1,1] <- want this high
false positives is C[0,1].
'''
def svcmodel(train_matrix, train_labels, test_labels):
	#Initialize Model
	model1 = LinearSVC()
	model1.fit(train_matrix, train_labels)
	result = model1.predict(test_matrix)
	# Results for LinearSVC() model
	c1 = confusion_matrix(test_labels,result)
	acc = (c1[0,0] + c1[1,1])/len(test_labels)
	return acc

def nbmodel(train_matrix, train_labels, test_labels):
	# Initialize model
	model2 = MultinomialNB()
	# Fitting the models for later use
	model2.fit(train_matrix, train_labels)
	result = model2.predict(test_matrix)
	# Results for MultinomialNB() model
	c2 = confusion_matrix(test_labels,result)
	acc = (c2[0,0] + c2[1,1])/len(test_labels)
	return acc

def models():
	# Test Email
	'''
	Lingspam_public data set
		- 4 categories
		- 10 parts each
		- Each part has 48 spam and 242 ham
	'''

	# File paths
	training2 = "./data/lingspam_public/bare/part1"
	testing1 = './data/lingspam_public/bare/part1'
	
	# =========================== TRAINING ===========================

	dictionary = count_words(training2) #Creates a dictionary containing frequencies of words.
	
	# Creating our labels, 1 indicates spam, 0 indicates ham
	train_labels = np.zeros(289)
	train_labels[241:288] = 1
	train_matrix = extract_features(training2, dictionary)


	# ============================ TESTING ===========================
	# Testing unseen data
	test_matrix = extract_features(testing1, dictionary)
	
	# Creating our labels, 1 indicates spam, 0 indicates ham
	test_labels = np.zeros(289)
	test_labels[241:288] = 1

	c1_acc = svcmodel(train_matrix, train_labels, test_labels)
	c2_acc = nbmodel(train_matrix, train_labels, test_labels) 

	# ============================ RESULTS ===========================
	print("Support Vector Classification Accuracy:", c1_acc)
	print("Naive Bayes Accuracy:", c2_acc)

def main():
	models()

if __name__ == '__main__':
	main()



