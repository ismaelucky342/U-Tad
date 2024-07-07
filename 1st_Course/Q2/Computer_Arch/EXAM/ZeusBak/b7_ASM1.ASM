; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+

Operando1:  DEFB 5        ; Definir y asignar el valor 5 a Operando1
Operando2:  DEFB -9       ; Definir y asignar el valor -9 a Operando2
Operando3:  DEFB 0        ; Definir y asignar el valor 0 a Operando3
; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                    ; Start of application

AppEntry                LD A, (Operando1)               ; Cargar en el acumulador el contenido de Operando1
                        ADD A, (Operando2)              ; Sumar el contenido de Operando2
                        SLA A                           ; Desplazar un bit a la izquierda el acumulador
                        CPL                             ; Complementar a 1 el acumulador
                        INC A                           ; Completar el complemento a 2 del resultado

                        CP 8                            ; Comparar con el número 8
                        CALL Z, ResComp                 ; Llamar a la subrutina ResComp si el resultado es igual


ResComp:
                        LD A, 1                         ; Cargar el número 1 en el acumulador
                        JR Z, Almacenar                 ; Saltar a Almacenar si Z está activo (resultado es igual a 8)

                        LD A, 2                         ; Cargar el número 2 en el acumulador

Almacenar:
                        LD (Operando3), A               ; Guardar el valor en Operando3
                        RET                             ; Retornar de la subrutina

                        halt                            ; Replace these lines with your code
                        jp AppEntry                     ;

Operando1:              DEFB 5                          ; Definir y asignar el valor 5 a Operando1
Operando2:              DEFB -9                         ; Definir y asignar el valor -9 a Operando2
Operando3:              DEFB 0                          ; Definir y asignar el valor 0 a Operando3

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


