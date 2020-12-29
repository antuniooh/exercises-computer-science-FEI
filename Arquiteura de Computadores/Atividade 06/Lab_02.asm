CONFIG:
	MOV TMOD,#1 ;CT0 no modo 1
	MOV TH0,#0FCh ;valor para a recarga
	MOV TL0,#18h;valor para a primeira contagem
	SETB TR0 ;liga o CT0
	SETB P1.0

LB1:
	JNB TF0,$ ;aguarda bit de ultrapassagem
	MOV TH0,#0D8h ;valor para a primeira contagem
	MOV TL0, #0F0h
	CLR TF0 ;apaga bit de ultrapassagem
	CLR P1.0 ;faz P1.0 = 0
LB2:
	JNB TF0,$ ;aguarda bit de ultrapassagem
	CLR TF0 ;apaga bit de ultrapassagem
	SETB P1.0 ;faz P1.0 = 1
	MOV TH0,#0F2h ;valor para a recarga
	MOV TL0,#53h;valor para a primeira 
LB3:
	JNB TF0,$ ;aguarda bit de ultrapassagem
	MOV TH0,#0E4h ;valor para a primeira contagem
	MOV TL0, #0A8h
	CLR TF0 ;apaga bit de ultrapassagem
	CLR P1.0 ;faz P1.0 = 0
LB4:
	JNB TF0,$ ;aguarda bit de ultrapassagem
	CLR TF0
	SETB P1.0 
	SJMP LB1 ;volta para LB1: 
