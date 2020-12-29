;SETB C
;jc DESVIO
;mov 00h, C

;DESVIO:
;cpl C
;mov 00h, C

;mov R0, #07h
;mov R1, #00h

;djnz R0, CONTA; decrement e ve se é diff 0
;sjmp SAIDA

;CONTA:
;inc R1

;SAIDA:
;nop

;LCALL FUNC

;FUNC:
;INC R0
;RET

;CLR A
;MOV R0, #127

;ROT:
;MOV @R0, A
;DJNZ R0, ROT
;RET

;COMP:
;MOV A, R7 ;E8 + 7
;CLR C; C3
;SUBB A, R6; 9E
;JNC ROT1; 50

;XCH A, R7; CF
;XCH A, R6; CE
;XCH A,R7; CF

;ROT1:
;SJMP $

;COMP:
;MOV A, R7
;CLR C; zera o carry
;SUBB A, R6
;a -r6, se c =0, a >= R6
;a -r6; se c =1, a < r6

;JNC ROT1; C ==0, finaliza
;XCH A, R7
;XCH A, R6; faz a troca
;XCH A, R7
;ROT1:
;SJMP $


