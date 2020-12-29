ORG 0				; reset vector
	JMP main		; jump to the main program

ORG 03h				; external 0 interrupt vector
	JMP ext0ISR		; jump to the external 0 ISR

ORG 30H				; main program starts here
main:
	SETB IT0		; set external 0 interrupt as edge-activated
	SETB EX0		; enable external 0 interrupt
	SETB EA			; set the global interrupt enable bit
rot:
	CLR P3.6		; clear ADC WR line
	SETB P3.6		; then set it - this results in the required positive edge to start a conversion
	CALL delay
	JMP rot

; end of main program


; external 0 ISR - responds to the ADC conversion complete interrupt
ext0ISR:
	CLR P3.7		; clear the ADC RD line - this enables the data lines
	MOV P1, P2		; take the data from the ADC on P2 and send it to the DAC data lines on P1
	SETB P3.7		; disable the ADC data lines by setting RD
	RETI			; return from interrupt

delay:
	MOV R0, #40
	DJNZ R0, $
	RET