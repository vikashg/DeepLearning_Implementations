import numpy as np
from random import seed
from random import random 

#Step 1: Initialize a network 
# Here num_input, num_hidden, num_output are the NUMBER OF NEURONS in the input, hidden and output layers and NOT the number of layers.
def initialize_network( num_input, num_hidden, num_output):
	network = list() #Define an empty list of parameters
	#for i in range(num_hidden):
	hidden_layer = [{'weights': np.random.rand( num_input + 1, num_hidden)}]
	network.append(hidden_layer)
	output_layer = [{'weights': np.random.rand(num_hidden + 1, num_output)}]
	network.append(output_layer)
	return network
	
if __name__=='__main__':
	network = initialize_network(2,1,2)
	print (network)
