CONFIG:
	MOV TMOD, #2; CT0 no mod 2
	MOV TH0, #2066; valor para a recarga
	MOV Tl0, #2066; valor para a primeira contagem
	SETB TR0; liga po Ct0
	SETB P1.0; incia o primeio perido

LB1:
	JNB TF0, $; aguarda o overflow
	MOV TL0, #6; valor para a primeira recarga
	CLR TF0; apaga o overflow
	CLR P1.0; p1.0 = 0

LB2:
	JNB TF0, $; aguarda o overflow
	CLR TF0; apaga o overflow
	SETB P1.0;faz p1.0 = 1
	SJMP LB1; pula para o rot