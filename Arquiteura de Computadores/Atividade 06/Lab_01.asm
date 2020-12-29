CONFIG:
	MOV TMOD,#2 ;CT0 no modo 2
	MOV TH0,#156 ;valor para a recarga
	MOV TL0,#156 ;valor para a primeira contagem
	SETB TR0 ;liga o CT0
ROT:
	JNB TF0,$ ;aguarda bit de ultrapassagem
	CLR TF0 ;apaga bit de ultrapassagem
	CPL P1.0 ;complementa P1.0

ROT1:
	MOV TH0, #101
	MOV TL0, #101
	JNB TF0,$ ;aguarda bit de ultrapassagem
	CLR TF0 ;apaga bit de ultrapassagem
	CPL P1.4 ;complementa P1.4
	SJMP ROT ;fecha o laço