org 0000h
	LJMP START

org 000Bh
INT_TEMP0:
	MOV TH0,#156 ;valor para a recarga
	MOV TL0,#156 ;valor para a primeira cont
	CPL P1.0
	RETI

org 001Bh
INT_TEMP1:
	MOV TH1,#101 ;valor para a recarga
	MOV TL1,#101 ;valoimeira contagem
	CPL P1.4
	RETI
org 0080h
START:
	MOV TMOD,#22h
	MOV TH0,#156 ;valor para a recarga
	MOV TL0,#156 ;valor para a primei
	MOV TH1,#101 ;valor para a recarga
	MOV TL1,#101 ;valoimeira contagem
	SETB EA
	SETB ET0
	SETB ET1
	SETB TR0
	SETB TR1
	SJMP $

