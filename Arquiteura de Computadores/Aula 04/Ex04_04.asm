DELAY:
	MOV R0, #84; 1

ROT1:
	MOV R1, #58

ROT2:
	DJNZ R1, ROT2; 2*R1
	DJNZ R0, ROT1; (1+2*R1+2)*R0
	nop; 1
RET; 2

;T = 1+[1 + (2x58) + 2]x84 + 1 +3 = 10000MC
