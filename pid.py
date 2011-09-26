import matplotlib.pyplot as plt
from numpy import array

arm_length = 0.254
mass = 1.2

def calc_motors(state, gains):
	return gains.dot(state[0].transpose())

def update_state(state, motors, dt):
	roll_accel = ((motors[0] - motors[2]) * arm_length) / mass
	pitch_accel = ((motors[1] - motors[3]) * arm_length) / mass

	# integrate state vel and add to state
	state[0] += state[1]*dt 

	# update state velocity
	state[1][0] += roll_accel*dt
	state[1][1] += roll_accel*dt

	return state

def run_sim(start_state, gains, time, dt):
	states = [start_state,]
	cur_time = 0.0
	cur_state = start_state
	while cur_time <= time:
		cur_state = cur_state.copy()
		motors = calc_motors(cur_state, gains)
		cur_state = update_state(cur_state, motors, dt)
		states.append(cur_state)
		cur_time += dt
	return states
	
if __name__=='__main__':
	# [Roll, Pitch, Yaw, Vertical] motor1
	# [ ..                       ] motor2
	# [ ..                       ] motor3
	# [ ..                       ] motor4
	gains = array([[-1.0, 0, 0, 0],
	               [-1.0, 0, 0, 0],
	               [1.0, 0, 0, 0],
	               [1.0, 0, 0, 0]])

	# Start state
	# [Roll, Pitch, Yaw, Vertical]
	# [ ..                       ] dt
	state = array([[1.0, 0, 0, 0],
	               [0, 0, 0, 0]])
	
	
	states = run_sim(state, gains, 50, .1)
	roll_vals = [s[0][0] for s in states]
	plt.plot(range(len(roll_vals)),roll_vals)
	plt.show()

