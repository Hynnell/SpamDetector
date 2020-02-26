import numpy as np
from extract import *
from normalize import *

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
    for i in range(numex):
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


# Load train and test data.  Learn model.  Report accuracy.
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

  #Normalizing data here
  # train_x, test_x = rangenorm(train_x, test_x)
  # train_x, test_x = varnorm(train_x, test_x)
  # train_x, test_x = exnorm(train_x, test_x)

  # Creating our labels, 1 indicates spam, -1 indicates ham
  train_y = np.zeros(289)
  train_y[0:240] = -1
  train_y[241:288] = 1

  # Creating our labels, 1 indicates spam, -1 indicates ham
  test_y = np.zeros(289)
  test_y[0:240] = -1
  test_y[241:288] = 1

  (w,b) = train_perceptron(train_x, train_y, maxiter=100)

  correct = 0
  for (x,y) in zip(test_x, test_y):
    activation = predict_perceptron( (w,b), x )
    if activation * y > 0:
      correct += 1
  acc = float(correct)/len(test_y)
  print("Accuracy: ",acc)


if __name__ == "__main__":
  main()
