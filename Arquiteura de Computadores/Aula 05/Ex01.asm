MOV A, #0fh

ROT:
	PUSH ACC
	DEC A
	JNZ ROT; a nao for zero