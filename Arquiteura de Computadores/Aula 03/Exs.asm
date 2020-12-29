;MOV A, R1
;ADD A, R0
;MOV R7, A

;upcode
;E8+1 ;mov a, r1 = E9
;28+0 ;add a, r0 = 28
;F8+7 ;mov r7, a  =FF

;MOV A, R0 = E8+0 = E8
;MOV B, R1 = 89 FO
;MUL AB = A4
;MOV R6, A = F8 + 6 = FE
;MOV R7, B = AF FO

;MOV A, R1 ; - E8 +1 = E9
;MOV B, R0 ; 88 FO
;DIV AB  ;84
;a -quociente, b- resto
;MOV R7, A; FF
;MOV R6, B; AE F0

;MOV A,R1; = E8 +1 = E9
;ADDC A, R0; 28
;MOV R6, A; LSB = F8 + 6 = FE
;CLR A; E4
;ADDC A, #0; 34 00
;MOV R7, A ;R7 MSL = F8 + 7 = FF

;MOV A,R2; copia para o A o LSB
;ADD A, R0; soma com o LSB de R0
;MOV R5, A; copia o LSB do resultado PRa R5
;MOV A, R3; copia o MSB do 1 numero 
;ADDC A,R1; soma com o MSB do 2 numero com carry
;MOV R6, A; copia para R6
;CLR A; zera
;ADDC A, #0; soma zero ao a mais carry
;MOV R7, A; copia o resutado pra R7

;R3 R2 - R1 R0
MOV A, R2
CLR C;carry
SUBB A, R0; subtrai o LSB
MOV R6, A; copia o lsb do resultado
MOV A, R3; copia para o acumulador o msm do minuend
SUBB A, R1; subtrai o msb do subtraend com borroe
MOV R7, A; copia o msb do resultado´para r7