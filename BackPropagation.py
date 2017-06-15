import numpy as np
from random import seed
from random import random 


#Step 1: Initialize a network 
# Here num_input, num_hidden, num_output are the NUMBER OF NEURONS in the input, hidden and output layers and NOT the number of layers.
def initialize_network( num_input, num_hidden, num_output):
	network = list() #Define an empty list of parameters
	for i in range(num_hidden):
		hidden_layer = [{'weights': np.random.rand( num_input + 1, 1)}]
		network.append(hidden_layer)
	for i in range(num_output):
		output_layer = [{'weights': np.random.rand(num_hidden + 1, 1)}]
		network.append(output_layer)
	
	return network

#Step 2: Define Activation: Weighted sum of inputs 
def activate(weights, inputs):
	sum1 = np.sum(np.multiply(weights, inputs))
	return sum1

#Step 3: Define Transferfunction -- Sigmoid
def transferfunction(activation):
	result = 1/(1+np.exp(activation))
	return result
#Step 3: Define Fwd Propagation
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			print(activation)
			neuron['output'] = transferfunction(activation)
			
		new_inputs.append(neuron['output'])
	inputs = new_inputs
	
	return inputs	

if __name__=='__main__':
	network = initialize_network(2,1,2)
	input_ = np.full((1,1, 3), 2)
	#for i in range(3):
	#	print(network[i][0]['weights'])
	
	for layer in network:
		print(layer)
		for neuron in layer:
			print(neuron)
	#print(input_['input'])	
	#imp = forward_propagate(network, input_['input'])
	#SUM = activation(network[0][0]['weights'], input_['input'])
	#print(SUM)
	#input_ = np.array([1,0, None])
	print(type(input_))
	inputs = forward_propagate(network, input_)
	print(inputs)	
