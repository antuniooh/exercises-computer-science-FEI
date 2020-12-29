org 0000h
	LJMP START ;Pula incondicionalmente para START

org 000Bh
INT_TEMP0:
	CPL P1.7 ;complementa P1.7
	RETI ;Retorna da interrupção

org 0080h
START:
	MOV TMOD,#00001110b ;Usa modo 02 e Habilita o Contador
	MOV TH0, #236 ;valor para a recarga
	MOV TL0, #236 ;valor para a contagem
	SETB EA ;Habilita as interrupções
	SETB ET0 ;Habilita o temporizador 0
	SETB TR0 ;Liga o temporizador
	SJMP $ ;Laço de repetição