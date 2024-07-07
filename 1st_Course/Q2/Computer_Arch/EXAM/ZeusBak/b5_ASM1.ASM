; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+


; Start planting code here. (When generating a tape file we start saving from here)

                        org 100h                        ; Start of application
; Lista 1
Lista1:
                        DB 08h, 04h, 1Ah, 11h, 10h      ;

; Lista 2
Lista2:
                        DB 11h, 26h, 04h, 0Fh, 0Eh      ;

; Variables para almacenar las sumas y el resultado de la comparación
Suma1:
                        DS 1                            ; Reservar 1 byte para Suma1
Suma2:
                        DS 1                            ; Reservar 1 byte para Suma2
Compara:
                        DS 1                            ; Reservar 1 byte para Compar
AppEntry                LD HL, Lista1                   ; Cargar la dirección de la primera lista en HL
                        LD DE, 5                        ; Número de elementos en la lista
                        LD A, 0                         ; Inicializar el acumulador A a 0
                        LD B, A                         ; B = 0 (para la suma)

Suma_Lista1:
                        ADD A, (HL)                     ; Sumar el valor en la dirección apuntada por HL al acumulador A
                        INC HL                          ; Incrementar HL para apuntar al siguiente número
                        DEC DE                          ; Decrementar DE
                        JR NZ, Suma_Lista1              ; Repetir hasta que DE sea 0
                        LD (Suma1), A                   ; Guardar el resultado de la suma en Suma1

                        LD HL, Lista2                   ; Cargar la dirección de la segunda lista en HL
                        LD DE, 5                        ; Número de elementos en la lista
                        LD A, 0                         ; Inicializar el acumulador A a 0
                        LD B, A                         ; B = 0 (para la suma)

Suma_Lista2:
                        ADD A, (HL)                     ; Sumar el valor en la dirección apuntada por HL al acumulador A
                        INC HL                          ; Incrementar HL para apuntar al siguiente número
                        DEC DE                          ; Decrementar DE
                        JR NZ, Suma_Lista2              ; Repetir hasta que DE sea 0
                        LD (Suma2), A                   ; Guardar el resultado de la suma en Suma2

; Comparar Suma2 con Suma1
                        LD A, (Suma2)                   ; Cargar Suma2 en el acumulador A
                        CP (Suma1)                      ; Comparar A con el valor en Suma1
                        JR C, MenorOIgual               ; Si A < (Suma1), saltar a MenorOIgual
                        LD A, 1                         ; A = 1 (Suma2 > Suma1)
                        JR GuardarComparacion           ;

MenorOIgual:
                        LD A, -1                        ; A = -1 (Suma2 <= Suma1)

GuardarComparacion:
                        LD (Compara), A                 ; Guardar el resultado de la comparación en Compara


                        halt                            ; Replace these lines with your code
                        jp AppEntry                     ;


; Stop planting code after this. (When generating a tape file we save bytes below here)
AppLast                 equ *-1                         ; The last used byte's address

; Generate some useful debugging commands

                        profile AppFirst,AppLast-AppFirst+1 ; Enable profiling for all the code

; Setup the emulation registers, so Zeus can emulate this code correctly

Zeus_PC                 equ AppEntry                    ; Tell the emulator where to start
Zeus_SP                 equ $FF40                       ; Tell the emulator where to put the stack

; These generate some output files

                        ; Generate a SZX file
                        output_szx AppFilename+".szx",$0000,AppEntry ; The szx file

                        ; If we want a fancy loader we need to load a loading screen
;                        import_bin AppFilename+".scr",$4000            ; Load a loading screen

                        ; Now, also generate a tzx file using the loader
                        output_tzx AppFilename+".tzx",AppFilename,"",AppFirst,AppLast-AppFirst,1,AppEntry ; A tzx file using the loader


