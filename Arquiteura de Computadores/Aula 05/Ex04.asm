MOV A, #0fh
MOV 50h, #0ffh
MOV SP, #2Fh

ROT:
	PUSH 50h
	DEC A
	JNZ ROT; a nao for zero
	PUSH 50h