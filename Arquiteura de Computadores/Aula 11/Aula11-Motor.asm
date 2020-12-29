org 0000h
	LJMP MAIN

org 001Bh
int01:
	CPL P3.0   ;|
	CPL P3.1   ;| Inverte o sentido de rotação do motor
	RETI

org 0030h
MAIN:
	MOV TMOD, #01100000b  ;Contador CT1 no modo 2
	SETB EA							;Habilita as interrupções
	SETB ET1         			;Habilita a interrupção CT1
	SETB TR1						;Liga o contador 1
	SETB P3.0        			;|
	CLR  P3.1						;| Liga motor no sentido horário
	JMP $