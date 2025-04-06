; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+


; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                    ; Start of application

AppEntry                ld hl, 8100h                    ; HL apunta a la dirección 8100h
                        ld b, 1                         ; B contiene el número inicial (1)
                        ld c, 3                         ; C contiene el número de iteraciones (3 veces)

loop ld a, b                                            ; A contiene el número actual
                        add a, a                        ; Doble del número actual (A = B * 2)
                        ld (hl), a                      ; Guarda el doble en la memoria (HL)
                        inc hl                          ; Incrementa HL para la siguiente posición
                        ld a, b                         ; A contiene el número actual
                        add a, b                        ; Suma el número actual (B) a sí mismo
                        add a, 1                        ; A + 1
                        ld (hl), a                      ; Guarda el valor en la memoria (HL)
                        inc hl                          ; Incrementa HL para la siguiente posición
                        add a, b                        ; Doble el número original (B) en A
                        ld b, a                         ; B ahora contiene el nuevo número
                        dec c                           ; Decrementa el contador de iteraciones
                        jr nz, loop                     ; Repite el bucle si C no es cero

fin                     halt                            ; Detiene la CPU
                        jp AppEntry                     ; Bucle infinito para detener la ejecución


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


