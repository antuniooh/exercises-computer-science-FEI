CONFIG:
	MOV TMOD, #1; CT0 no mod 1
	MOV TH0, #0F8h; valor para a recarga
	MOV Tl0, #30h; valor para a primeira contagem
	SETB TR0; liga po Ct0

ROT:
	JNB TF0, $; aguarda o overflow
	MOV TH0, #0F8h; valor para a primeira recarga
	MOV TL0, #30h
	CLR TF0; apaga o overflow
	CPL P1.0; complementa o p1
	SJMP ROT; fecha o lçao