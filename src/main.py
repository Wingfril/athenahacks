import dataprocessing
import tensor

def init():
	data = dataprocessing.makeDictionary()
	eqs = tensor.train(data)
	return eqs

def compute(temp, eqs):
	result = {}
	for state in eqs.keys():
		result[state] = tensor.evaluate(temp, eqs[state])
	return result
