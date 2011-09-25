import matplotlib.pyplot as plt
from numpy import array

calc_output = lambda state, gains: gains * state[0].transpose()
	
if __name__=='__main__':
	# [Roll, Pitch, Yaw, Vertical] P
	# [ ..                       ] D
	# [ ..                       ] I
	gains = array([0, 0, 0, 0],
	              [0, 0, 0, 0],
	              [0, 0, 0, 0])

	# Start state
	# [Roll, Pitch, Yaw, Vertical]
	# [ ..                       ] dt
	state = array([0, 0, 0, 0, 0],
	              [0, 0, 0, 0, 0])
	
	
	

