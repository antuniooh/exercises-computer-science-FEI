DELAY:
	MOV R0, #195; 1

ROT1:
	MOV R1, #41;1

ROT2:
	DJNZ R1, ROT2; 2*R1
	DJNZ R0, ROT1; (1+2*R1+2)*R0
	nop;1
	nop;1
RET; 2

;T = 5 + [2*41 + 3] * 195 = 8000
