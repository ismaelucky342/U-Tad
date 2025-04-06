; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+


; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                    ; Start of application

AppEntry                ld B, 5                         ; Carga el registro B con el valor 5 (cantidad de elementos a comparar)
                        ld IX, num1                     ; Carga el registro IX con la dirección de la lista num1
bucle                   ld C, (IX)                      ; Carga el registro C con el valor apuntado por IX (elemento actual de num1)
                        ld D, (IX + 5)                  ; Carga el registro D con el valor de la lista num2 en la misma posición (elemento actual de num2)
                        call compara                    ; Llama a la subrutina de comparación
                        ld (IX + 10), A                 ; Guarda el resultado de la comparación en la posición correspondiente de res2
                        inc IX                          ; Incrementa IX para apuntar al siguiente elemento de num1
                        djnz bucle                      ; Decrementa B y si no es cero, salta a bucle (repite el ciclo)
                        jp fin                          ; Salta a la etiqueta fin (termina el programa)


compara                 LD A, D                         ; Carga el valor de D en el registro A (preparación para la comparación)
                        CP C                            ; Compara el valor de A con C (A - C)
                        JP Z, iguales                   ; Si A y C son iguales (Z flag set), salta a la etiqueta iguales
                        JP NC, mayor                    ; Si A >= C (NC flag set), salta a la etiqueta mayor
                        LD A, -1                        ; Si A < C, carga -1 en A
                        RET                             ; Retorna de la subrutina
iguales                 LD A, 0                         ; Carga 0 en A (si los valores son iguales)
                        RET                             ; Retorna de la subrutina
mayor                   LD A, 1                         ; Carga 1 en A (si A > C)
                        RET                             ; Retorna de la subrutina


fin                     halt                            ; Detiene la ejecución del programa
                        jp fin                          ; Bucle infinito para detener el programa

num1                    defb 1,1,2,2,3                  ; Define la lista num1 con los valores 1, 1, 2, 2, 3
num2                    defb 3,3,2,2,1                  ; Define la lista num2 con los valores 3, 3, 2, 2, 1
res2                    defs 5                          ; Reserva 5 bytes en memoria para almacenar los resultados de la comparación


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


