; examples 

; Extended Addresing

; Load the content of memory address 0C745H into register A
LD A, (0C745H)


; Indirect Addressing:

; Assuming HL holds the memory address where the data is stored
; Load the content of the memory address pointed to by HL into register A
LD A, (HL)

; Indexed Addressing:

; Assuming IX holds the base address and B holds the offset
; Load the content of memory address (IX + B) into register A
LD A, (IX+B)

; Register Indirect Addressing

; Assuming the desired data is already in register B
; Move the content of register B into register A
LD A, B

; Implicit Addressing:

; The instruction ADD A, B adds the content of A and B and stores the result in A
ADD A, B

; Immediate Addressing

; Load the immediate value 42 into register A
LD A, 42

; Extended Inmediate Addresing

; Load the extended immediate value 1234H into registers DE
LD DE, 1234H
