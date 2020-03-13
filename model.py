#=============================Imports==============================#

import numpy as np
from extract import *
from normalize import *
# import ui as u
#==================================================================#


#=============================KNN Model============================#

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

#==================================================================#






#=========================Perceptron Model=========================#

# Learn weights using the perceptron algorithm
def train_perceptron(train_x, train_y, maxiter=100):
  # Initialize weight vector and bias
  '''
  Check whether or not a point is correctly classified
  If it is: 
    Do nothing
  If it is not: 
    Figure out which weight (wi) is affected it most and adjust by accordingly.


  '''
  numvars = len(train_x[0])
  numex = len(train_x)
  w = np.array([0.0] * numvars)
  b = 0.0

  for m in range(maxiter):
    for i in range(numex-1):
      a = np.dot(w, train_x[i]) + b #Compute activation

      a = a * train_y[i]
      # print(a)
      if a <= 0: # There is something wrong, we need to update. 

        # Iterate through w, add the product of xj and yj
        for j in range(numvars):
          update = np.dot(train_y[i], train_x[i][j])
          w[j] = w[j] + update

        b = b + train_y[i] # Update the bias
        
      # Else: No update needed (correct prediction)

  # print((w,b))
  return (w,b)

def predict_perceptron(model, x):
  (w,b) = model

  a = 0
  for i in range(len(x)):
    a += w[i]*x[i]

  a += b
  return a


#==================================================================#






#=================================Model============================#
# Type of model (1 = KNN, 2 = Perceptron, directory of training, directory of testing,
# Total numbers of files, total numbers of ham, single entry to be scanned
def model(model, default, training, testing, tot, ham, single):

	# =================== File I/O ====================

	# File Paths for default datasets
	if default:
		training = "./data/lingspam_public/bare/part1"
		testing = "./data/lingspam_public/bare/part2"

	# For testing purposes
	single_ham = "./data/test_ham.txt"
	single_spam = "./data/test_spam.txt"


	# # File Paths for Perceptron
	# training_p = "./data/lingspam_public/bare/part1"
	# testing_p = "./data/lingspam_public/bare/part2"

	# =================================================


	# =============== Feature Extraction ==============

	# Read data from training
	final_words_train = count_words(training)
	train_x = extract_features(training, final_words_train)
	
	# Read data from testing
	final_words_test = count_words(testing)
	test_x = extract_features(testing, final_words_test)

	#Normalizing data here
	# train_x, test_x = rangenorm(train_x, test_x)
	# train_x, test_x = varnorm(train_x, test_x)
	# train_x, test_x = exnorm(train_x, test_x)

	# =================================================


	# ============================Single Email============================

	test_dict = read_dict()

	# print("Starting dictionary extraction")
	# for i in range(len(test_dict)):
	# 	if test_dict[i] != final_words_train[i][0]:
	# 		print(test_dict[i], final_words_train[i][0])
	# print("Dictionary extraction done")

	ham_vector = extract_single(single_ham)

	# print("Extracted ham_vector is:", ham_vector)
	# print("Length of ham_vector is:", len(ham_vector))
	# print("train_x[0] is:", train_x[0])
	# print("Length of train_x[0] is:", len(train_x[0]))

	# print("Testing single email")
	# count = 0
	# for i in range(len(ham_vector)):
	# 	# print(ham_vector[i], train_x[0][i])
	# 	if ham_vector[i] != train_x[0][i]:
	# 		count += 1
	# 		print("Error^^^")
	# print("Single email testing complete.")
	# print("Final count is:", count)

	# ====================================================================


	# ==================== Storage ====================

	store_dict(final_words_train) #Store the feature matrix in data.txt
	new_words = read_dict()

	store_matrix(train_x) # Store the feature matrix in matrix.txt
	new_matrix = read_matrix()

	#Checking storage
	# print("Retrieving from storage.")

	# for i in range(len(new_matrix)):
	# 	for j in range(len(new_matrix[0])):
	# 		if train_x[i][j] != new_matrix[i][j]:
	# 			print("Not the same in storage.")

	# print("Done retrieving from storage.")

	# =================================================
	if default:
		# Creating our labels, 1 indicates spam, -1 indicates ham
		train_y = np.zeros(289)
		train_y[0:240] = -1
		train_y[241:288] = 1

		# Creating our labels, 1 indicates spam, -1 indicates ham
		test_y = np.zeros(289)
		test_y[0:240] = -1
		test_y[241:288] = 1
	else:
		# Creating our labels, 1 indicates spam, -1 indicates ham
		train_y = np.zeros(tot)
		train_y[0:(ham-1)] = -1
		train_y[ham:(tot-1)] = 1

		# Creating our labels, 1 indicates spam, -1 indicates ham
		test_y = np.zeros(tot)
		test_y[0:(ham-1)] = -1
		test_y[ham:(tot-1)] = 1

	if model == 1:


		#===============================KNN==================================


		k = 6
		print("Starting KNN testing")
		acc = runTest(test_x, test_y, train_x, train_y, k)
		print("KNN testing done")
		print("Accuracy:", acc)

		predict1 = classify(new_matrix, train_y, 1, ham_vector)
		# print("Ham Predication:", predict1)

		spam_vector = extract_single(single_spam)
		predict2 = classify(new_matrix, train_y, 1, spam_vector)
		# print("Spam Predication:", predict2)

		return acc

		#====================================================================

	

	elif model == 2:

		#============================Perceptron==============================

		# # Creating our labels, 1 indicates spam, -1 indicates ham
		# train_y = np.zeros(289)
		# train_y[0:240] = -1
		# train_y[241:288] = 1

		# # Creating our labels, 1 indicates spam, -1 indicates ham
		# test_y = np.zeros(289)
		# test_y[0:240] = -1
		# test_y[241:288] = 1

		(w,b) = train_perceptron(train_x, train_y, 100)

		correct = 0
		for (x,y) in zip(test_x, test_y):
			activation = predict_perceptron( (w,b), x )
			if activation * y > 0:
				correct += 1
		acc = float(correct)/len(test_y)
		# print("Accuracy: ",acc)
		return acc

		#====================================================================


	else:
		print("Not a valid model (1 for KNN, 2 for Perceptron).")

	#NOTE THIS ONLY RETURNS ONE PREDICTION
	return predict1

#==================================================================#

# For testing

# model(1, 1, "", "", 0, 0, 0)

















