MOV A, #0fh
MOV 030h, #0ffh

ROT:
	PUSH 030h
	DEC A
	JNZ ROT; a nao for zero