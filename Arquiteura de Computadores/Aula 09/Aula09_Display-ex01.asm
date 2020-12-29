start:
	MOV P3, #11111111b	; HABILITA display 3
	MOV P1, #0F9h		; Apresenta 1 no display
	CALL delay
	MOV P3, #11110111b 	; HABILITA display 2
	MOV P1, #0A4h		; Apresenta 2 no display
	CALL delay
	MOV P3, #11101111b 	; HABILITA display 1
	MOV P1, #0B0h		; Apresenta 3 no display
	CALL delay
	MOV P3, #11100111b	; HABILITA display 0
	MOV P1, #099h		; Apresenta 4 no display
	CALL delay
	JMP start			; Salta para o start

delay:
	MOV R0, #250
	DJNZ R0, $
	RET
