org 0080h
ljmp MAIN
DELAY:
	MOV R7, #248; 1

ROT:
	DJNZ R7, ROT; 2*R7
	nop; 1
RET; 1

org 0020h
MAIN:
	call DELAY
	NOP
	sjmp $