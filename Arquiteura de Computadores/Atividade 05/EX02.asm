MOV  30h, #2h
MOV  31h, #2h
MOV  32h, #1h
MOV  33h, #1h
MOV  34h, #9h
MOV  35h, #0h
MOV  36h, #0h
MOV  37h, #1h
MOV  38h, #0h

READ:
	MOV R0, #30h; inicip
	MOV R1, #9h; tamanho do vetor

ROT2:
	MOV A, @R0
	ACALL CONFERE
	INC R0
	DJNZ R1, ROT2
	SJMP $

CONFERE:
	;confere se o valor q esta em R6
	;é maior do q o do acumulador
	CLR C
	MOV R6, A; variavel temp
	SUBB A, 39h
	JNC SUBSTITUI
	RET

SUBSTITUI:
	MOV 39h, R6
	RET
