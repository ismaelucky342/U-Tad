; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+


; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                    ; Start of application

AppEntry:
                        ld b, 4                         ; Carga el valor 4 en el registro B (contador de bucle)
                        ld hl, cadena                   ; Carga la dirección de la cadena en el registro HL

bucle:
                        ld a, (hl)                      ; Carga el byte apuntado por HL en el registro A
                        push af                         ; Guarda el valor de A en la pila
                        inc hl                          ; Incrementa HL para apuntar al siguiente byte
                        djnz bucle                      ; Decrementa B y salta a 'bucle' si B no es cero

                        ld b, 4                         ; Vuelve a cargar el valor 4 en B (contador de bucle)
                        ld hl, invertida                ; Carga la dirección de 'invertida' en HL

bucle2:
                        pop af                          ; Recupera el valor de A desde la pila
                        ld (hl), a                      ; Almacena el valor de A en la dirección apuntada por HL
                        inc hl                          ; Incrementa HL para apuntar al siguiente byte
                        djnz bucle2                     ; Decrementa B y salta a 'bucle2' si B no es cero

fin:
                        halt                            ; Detiene la CPU
                        jp fin                          ; Salta a 'fin' (bucle infinito para detener la ejecución)

cadena:
                        defb "hola"                     ; Define la cadena "hola"
invertida:
                        defs 4                          ; Reserva 4 bytes para la cadena invertida
;
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


