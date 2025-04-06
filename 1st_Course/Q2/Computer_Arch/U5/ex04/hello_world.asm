; This is a basic template file for writing 48K Spectrum code.
; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "HelloWorld"                   ; What we're called (for file generation)

AppFirst                equ $8000                          ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"           ; Set the model and enable ULA+

; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                       ; Start of application

AppEntry:               call ClearScreen                   ; Llamar a la subrutina que limpia la pantalla
                        ld hl, Message                     ; Cargar la direcci�n del mensaje en HL
                        call 0x1601                        ; Llamar a la rutina de impresi�n del sistema operativo
                        ret                                ; Retornar al sistema operativo

ClearScreen:            ld hl, 16384                       ; Direcci�n de inicio de la pantalla
                        ld de, 16385                       ; Direcci�n siguiente
                        ld bc, 6143                        ; N�mero de bytes a limpiar
                        ld (hl), 0                         ; Escribir cero en la primera direcci�n
                        ldir                               ; Bloque de movimiento de memoria
                        ret                                ; Retornar al programa principal

Message:                db "Hola Mundo!", 0                ; Mensaje a imprimir

; Stop planting code after this. (When generating a tape file we save bytes below here)
AppLast                 equ *-1                            ; The last used byte's address

; Generate some useful debugging commands

                        profile AppFirst,AppLast-AppFirst+1     ; Enable profiling for all the code

; Setup the emulation registers, so Zeus can emulate this code correctly

Zeus_PC                 equ AppEntry                            ; Tell the emulator where to start
Zeus_SP                 equ $FF40                               ; Tell the emulator where to put the stack

; These generate some output files

                        ; Generate a SZX file
                        output_szx AppFilename+".szx",$0000,AppEntry    ; The szx file

                        ; If we want a fancy loader we need to load a loading screen
;                        import_bin AppFilename+".scr",$4000            ; Load a loading screen

                        ; Now, also generate a tzx file using the loader
                        output_tzx AppFilename+".tzx",AppFilename,"",AppFirst,AppLast-AppFirst,1,AppEntry ; A tzx file using the loader

