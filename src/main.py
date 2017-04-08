
import tensor

def main():
	#import_module('tensor')
	data = { 'alabama' : [[2000+x, 3*x, x] for x in range(5)]}
	tensor.train(data)

if __name__=='__main__': main()