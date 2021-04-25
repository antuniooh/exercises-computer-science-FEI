org 0000h
	LJMP START ;Pula incondicionalmente para S
org 000Bh
INT_TEMP0:
	MOV TH0, #0ECh ;valor para a recarga
	MOV TL0, #78h ;valor para a contag
	CPL P1.0 ;complementa P1.0
	RETI ;Retorna da interrupção
org 0080h
START:
	MOV TMOD,#1
	MOV TH0, #0ECh ;valor para a recarga
	MOV TL0, #78h ;valor para a contagem
	SETB EA ;Habilita as interrupções
	SETB ET0 ;Habilita o temporizador 0
	SETB TR0 ;Liga o temporizador
	SJMP $ ;Laço de repetição
