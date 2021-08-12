state_initial = "001"

# 010
# 0* | 1*
# 0*11+

accepted_states = [1, 4, 5, 6]
state = 1

def validate_state(state):
	if state in accepted_states:
		return True
	return False
	

if state_initial == "":
	print("Seu estado foi aceito: " + state_initial)
else:
	for char in state_initial:        
		if state == 0 and char == "0":
			state = 1
		if state == 0 and char == "1":
			state = 6

		elif state == 1 and char == "0":
			state = 1
		elif state == 1 and char == "1":
			state = 3

		elif state == 3 and char == "0":
			state = 4
		elif state == 3 and char == "1":
			state = 5
            
		elif state == 4 and char == "1":
			state = 7
		elif state == 4 and char == "0":
			state = 7

		elif state == 5 and char == "1":
			state = 5
		elif state == 5 and char == "0":
			state = 7
        
		elif state == 6 and char == "1":
			state = 6
		elif state == 6 and char == "0":
			state = 7


if validate_state(state):
	print("Seu estado foi aceito: " + state_initial)
else:
	print("Seu estado foi negado: " + state_initial)
