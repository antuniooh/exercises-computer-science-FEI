;ex 03
MOV R3, #08h
MOV R4, #03h

CLR A
mov A, R4
CLR C
SUBB A, R3
;r4 - r3 = 0, logo r4 >= r3
;r4 - r3 = 1, logo r4 < r3

;r6 menor
;r5 maior

JNC ROTR4MAIOR; c ==0
ROTR3MAIOR:
CLR A
MOV A, R3
MOV R5, A
CLR A
MOV A, R4
MOV R6, A
ACALL ROT1

JC ROTR3MAIOR; c == 1
ROTR4MAIOR:
CLR A
MOV A, R4
MOV R5, A
CLR A
MOV A, R3
MOV R6, A
ACALL ROT1

ROT1:
SJMP $