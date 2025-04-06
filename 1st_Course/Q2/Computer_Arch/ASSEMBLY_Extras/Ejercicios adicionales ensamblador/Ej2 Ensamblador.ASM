; This is a basic template file for writing 48K Spectrum code.

AppFilename             equ "NewFile"                   ; What we're called (for file generation)

AppFirst                equ $8000                       ; First byte of code (uncontended memory)

                        zeusemulate "48K","ULA+"        ; Set the model and enable ULA+


; Start planting code here. (When generating a tape file we start saving from here)

                        org AppFirst                    ; Start of application

AppEntry                ld B,1H                         ;
                        ld C,2H                         ;
                        ld D,3H                         ;
                        ld E,4H                         ;
                        ld H,5H                         ;
                        ld L,6H                         ;
                        ;ld IX,7H  ;este nos lo saltamos porque lo utilizamos luego                      ;
                        ld IY,8H                        ;

                        EXX                             ;
                        ;
                        ld B,9H                        ;
                        ld C,0AH                        ;
                        ld D,0BH                        ;
                        ld E,0CH                        ;
                        ld H,0DH                        ;
                        ld L,0EH                        ;

                        EXX                             ;

                        ld IX,8300H                      ;

                        ld (IX),A                       ;
                        inc IX                          ;
                        ld (IX),B                       ;
                        inc IX                          ;
                        ld (IX),C                       ;
                        inc IX                          ;
                        ld (IX),D                       ;
                        inc IX                          ;
                        ld (IX),E                       ;
                        inc IX                          ;
                        ld (IX),H                       ;
                        inc IX                          ;
                        ld (IX),L                       ;

                        EXX                             ;

                        inc IX                          ;                      ;
                        inc IX                          ;
                        ld (IX),B                       ;
                        inc IX                          ;
                        ld (IX),C                       ;
                        inc IX                          ;
                        ld (IX),D                       ;
                        inc IX                          ;
                        ld (IX),E                       ;
                        inc IX                          ;
                        ld (IX),H                       ;
                        inc IX                          ;
                        ld (IX),L                       ;
                        ;

                        halt                            ;
                        jp AppEntry                     ; Bucle infinito para poder verlo en el ejemplo                 ;


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


