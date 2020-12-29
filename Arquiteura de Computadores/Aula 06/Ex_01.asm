CONFIG:
	MOV TMOD, #2; CT0 no mod 2
	MOV TH0, #56; valor para a recarga
	MOV Tl0, #56; valor para a primeira contagem
	SETB TR0; liga po Ct0

ROT:
	JNB TF0, $; aguarda o overflow
	CLR TF0; apaga o overflow
	CPL P1.0; complemneta o p1
	SJMP ROT; pula para o rot