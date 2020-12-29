;zera a ram interna

ZERAR:
CLR A; A = 0
MOV R0, #127; R0 endereço mais alto

ROT:
MOV @R0, A; zera a posição apontada por r0
DJNZ R0, ROT; decerementa o ponteiro e o contador
RET; retorna

;1 MC
;1 MC
;1 MC (laço)
;2 MC (laço)
;2 MC

;4 + 127*3 = 385