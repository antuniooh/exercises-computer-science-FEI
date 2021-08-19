from os import stat


class Compiler:
	def __init__(self) -> None:
		self.accepted_states = [5, 8, 11, 13]
		self.state = 0

	def validate_state(self):
		if self.state in self.accepted_states:
			return True, "Palavra Reservada"
		return False, "what else"
	
	def check_word(self, word):
		for char in word:
			if self.state == 0 and char not in ["i", "e", "t","f"]:
				self.state = 14

			elif self.state == 0 and char == "i":
				self.state = 1
			elif self.state == 0 and char == "e":
				self.state = 2
			elif self.state == 0 and char == "t":
				self.state = 3
			elif self.state == 0 and char == "f":
				self.state = 4

			elif self.state == 1 and char == "f":
				self.state = 5

			elif self.state == 2 and char == "l":
				self.state = 6

			elif self.state == 3 and char == "h":
				self.state = 9

			elif self.state == 4 and char == "o":
				self.state = 12

			elif self.state == 6 and char == "s":
				self.state = 7

			elif self.state == 9 and char == "e":
				self.state = 10

			elif self.state == 12 and char == "r":
				self.state = 13

			elif self.state == 7 and char == "e":
				self.state = 8

			elif self.state == 10 and char == "n":
				self.state = 11

			elif self.state == 5 and char != "":
				self.state = 14
			elif self.state == 8 and char != "":
				self.state = 14
			elif self.state == 11 and char != "":
				self.state = 14
			elif self.state == 13 and char != "":
				self.state = 14
		
		self.check_validation()
		self.state = 0

	def check_validation(self):
		isValid, token = self.validate_state()
		if isValid:
			print("Seu estado foi aceito: (" + word + " " + str(token) + ")")
		else:
			print("Seu estado foi negado: (" + word + " " + str(token) + ")")

words = open("myfile.txt","r").read().split()
compiler = Compiler()
for word in words:
    compiler.check_word(word)
