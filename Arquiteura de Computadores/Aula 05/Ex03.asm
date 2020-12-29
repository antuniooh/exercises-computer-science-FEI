MOV A, #0fh

ROT:
	PUSH ACC
	DEC A
	JNZ ROT; a nao for zero

	MOV R2, #07h
	MOV R0, #70h

ROT2:
	POP ACC
	MOV @R0, A
	INC R0
	DJNZ R2, ROT2; r2 diferente de 0