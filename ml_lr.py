""" Linear Regression Machine Learning example:
###Uses data for machine age and time between failures###
###Predict a model for the data, supervised ML ####  """

## Import packages
import tensorflow as tf
import numpy
import pandas as pd
import matplotlib.pyplot as plt
rng = numpy.random

#Define your spreadsheet
spreadsheet = 'LR_ML.xlsx'
data = pd.read_excel(spreadsheet)

#Define your useful columns of data
months=data['Machine Age (Months)'].values
MTBF=data['Mean Time Between Failure (Days)'].values

# HyperParameters
learning_rate = 0.02
training_epochs = 3000

#Parameter
display_step = 50

# Training Data (X,Y) Sets
train_X = numpy.asarray(months)
train_Y = numpy.asarray(MTBF)

#Specifying the length of the train_x data
n_samples = train_X.shape[0]

# tf Graph Input --- Setting the dtype for the placeholder information
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights This is initializing the guesses of the model for weight and bias
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model (y=WX+b)
pred = tf.add(tf.multiply(X, W), b)

# Mean squared error This is the error in the calculation to try to minimize
error = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(error)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(error, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "error=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_error = sess.run(error, feed_dict={X: train_X, Y: train_Y})
    print("Training error=", training_error, "W=", sess.run(W), "b=", sess.run(b), '\n')

    # Graphic display
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()

    # Testing example, as requested (Issue #2)
    test_X = numpy.asarray([2,4,6,8,10])
    test_Y = numpy.asarray([25,23,21,19,17])

    print("Testing... (Mean square loss Comparison)")
    testing_error = sess.run(
        tf.reduce_sum(tf.pow(pred - Y, 2)) / (2 * test_X.shape[0]),
        feed_dict={X: test_X, Y: test_Y})  # same function as cost above
    print("Testing error=", testing_error)
    print("Absolute mean square loss difference:", abs(
        training_error - testing_error))

    plt.plot(test_X, test_Y, 'bo', label='Testing data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
