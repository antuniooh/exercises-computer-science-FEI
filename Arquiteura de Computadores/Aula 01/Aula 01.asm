;MOV A, #20h ; 32 em decimal
;MOV A, R0 ; recebe 0
;MOV A, R2 ; recebe 0
;MOV R2, A
;MOV 20h, A
;mov 21h, A

;mov R0, #25h
;mov A, #0ffh
;mov @R0, A ;endereçamento indireto

;mov R0, #27h
;mov A, #0ffh
;mov @R0, #21h
;mov A, @R0

;mov A, #20h
;ADD A, #20h
;psw é o carry bit, caso exceda 255

;mov A, #0ffh
;dec A; decrementa
;inc A; incrementa

;MOV R0, #10h
;MOV A, R0
;MOV 50h, #20h
;MOV R2, #10h
;INC R2
;DEC A
;MOV A, #0h