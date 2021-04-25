org 0000h
	LJMP START ;Pula incondicionalmente para START
	MOV R7, #0
org 0003h
INT_TEMP0:
	INC R7
	MOV P1, R7 ;complementa P1.0
	RETI ;Retorna da interrupção
org 0080h
START:
	SETB EA ;Habilita as interrupções
	SETB EX0 ;Habilita a interrupção 0
	SETB IT0 ;Trabalhando com borda de descida
	SJMP $ ;Laço de repetição
