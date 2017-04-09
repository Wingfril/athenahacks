import numpy as np
import tensorflow as tf

def train(data):
	result = {}
	# Model parameters
	a = tf.Variable([0.1], tf.float32)
	b = tf.Variable([0.1], tf.float32)
	c = tf.Variable([0.1], tf.float32)
	Z = tf.Variable([0.1], tf.float32)
	# Model input and output
	x = tf.placeholder(tf.float32)
	polynomial_model = a * x * x * x + b * x * x + c * x + Z
	y = tf.placeholder(tf.float32)
	# loss
	loss = tf.reduce_sum(tf.square(polynomial_model - y)) # sum of the squares
	# optimizer
	optimizer = tf.train.GradientDescentOptimizer(0.00000000000001)
	train = optimizer.minimize(loss)
	# training data
	for state in data.keys():
		x_train = []
		y_train = []
		for yearData in data[state]:
			x_train.append(yearData[1])
			y_train.append(yearData[2])
		# training loop
		init = tf.global_variables_initializer()
		sess = tf.Session()
		sess.run(init) # reset values to wrong
		for i in range(1000):
			sess.run(train, {x:x_train, y:y_train})
			
		# evaluate training accuracy
		curr_a, curr_b, curr_c, curr_Z, curr_loss  = sess.run([a, b, c, Z, loss], {x:x_train, y:y_train})
		print("%s: a: %s b: %s c: %s Z: %s loss: %s"%(state, curr_a, curr_b, curr_c, curr_Z, curr_loss))
		result[state] = [curr_a, curr_b, curr_c, curr_Z]
	return result

def evaluate(temp, const):
	return const[0]*math.pow(temp, 3) + const[1]*math.pow(temp, 2) + const[2]*temp + const[3]
