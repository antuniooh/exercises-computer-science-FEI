state_initial = "if"

# if
# else
# then
# for

accepted_states = [5, 8, 11, 13]
state = 0

def validate_state(state):
	if state in accepted_states:
		return True
	return False
	

if state_initial == "":
	print("Seu estado foi aceito: " + state_initial)
else:
	for char in state_initial:
		if state == 0 and char not in ["i", "e", "t","f"]:
			state = 14
			
		elif state == 0 and char == "i":
			state = 1
		elif state == 0 and char == "e":
			state = 2
		elif state == 0 and char == "t":
			state = 3
		elif state == 0 and char == "f":
			state = 4
		
		elif state == 1 and char == "f":
			state = 5

		elif state == 2 and char == "l":
			state = 6
		
		elif state == 3 and char == "h":
			state = 9

		elif state == 4 and char == "o":
			state = 12

		elif state == 6 and char == "s":
			state = 7

		elif state == 9 and char == "e":
			state = 10

		elif state == 12 and char == "r":
			state = 13

		elif state == 7 and char == "e":
			state = 8

		elif state == 10 and char == "n":
			state = 11

		elif state == 5 and char != "":
			state = 14
		elif state == 8 and char != "":
			state = 14
		elif state == 11 and char != "":
			state = 14
		elif state == 13 and char != "":
			state = 14

if validate_state(state):
	print("Seu estado foi aceito: " + state_initial)
else:
	print("Seu estado foi negado: " + state_initial)
