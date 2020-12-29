MOV R2, #0fh
MOV 50h, #0ffh
MOV SP, #2Fh

ROT:
	PUSH 50h
	DJNZ R2, ROT
	PUSH 50h
	MOV R2, #0Fh
	MOV R0, #70h

ROT2:
	POP ACC
	MOV @R0, A; o A recebe a pilha e passa pro 70
	INC R0	
	DJNZ R2, ROT2
	POP ACC
	MOV @R0, A