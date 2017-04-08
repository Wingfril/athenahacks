import tensorflow as tf

def init(data):
	sess = tf.Session()
	for state in data.keys():
		stateData = data[state]