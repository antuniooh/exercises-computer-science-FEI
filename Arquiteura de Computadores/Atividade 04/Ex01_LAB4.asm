ZERAR:
	CLR A; 1
	MOV R0, #99; 1

ROT:
	MOV @R0, A; 1
	NOP;1
	DJNZ R0, ROT; 99* (2 + 2)
RET;2

; 1 + 1 +99(4) + 2 = 400
