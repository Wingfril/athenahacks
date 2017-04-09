import dataprocessing
import tensor

def main():
	data = dataprocessing.makeDictionary()
	tensor.train(data)

if __name__=='__main__': main()
