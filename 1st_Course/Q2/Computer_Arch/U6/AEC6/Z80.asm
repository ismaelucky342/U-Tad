; Archivo de plantilla básico para escribir código de 48K Spectrum.

AppFilename             equ "ArrayComparison"            ; Nombre del archivo generado

AppFirst                equ $8000                        ; Primer byte del código (memoria no contenciosa)

                        zeusemulate "48K","ULA+"         ; Establece el modelo y habilita ULA+

                        org AppFirst                     ; Inicio de la aplicación

; Definición de los arrays
Array1                  db 1, 2, 3, 4, 5, 6, 7, 8, 9
Array2                  db 2, 2, 1, 1, 1, 9, 1, 1, 1
Results                 ds 9                             ; Array para almacenar los resultados (inicialmente vacío)

                        ld hl, Array1                    ; Apuntar al inicio de Array1
                        ld de, Array2                    ; Apuntar al inicio de Array2
                        ld bc, Results                   ; Apuntar al inicio del array de resultados
                        ld a, 9                          ; Longitud del array

CompareLoop:
                        ld a, (hl)                       ; Cargar elemento de Array1
                        ld b, (de)                       ; Cargar elemento de Array2

                        cp b                             ; Comparar A con B
                        jr z, StoreSeven                 ; Si A == B, almacenar 7
                        jr c, StoreDifference            ; Si A < B, almacenar diferencia
StoreSum:
                        add a, b                         ; A = A + B
                        ld (bc), a                       ; Guardar resultado en el array de resultados
                        jr NextElement

StoreDifference:
                        sub b                            ; A = A - B
                        ld (bc), a                       ; Guardar resultado en el array de resultados
                        jr NextElement

StoreSeven:
                        ld (bc), 7                       ; Almacenar 7 en el array de resultados

NextElement:
                        inc hl                           ; Siguiente elemento en Array1
                        inc de                           ; Siguiente elemento en Array2
                        inc bc                           ; Siguiente posición en el array de resultados
                        djnz CompareLoop                 ; Decrementar el contador y repetir si no es 0

; Búsqueda del valor 7 en el array de resultados
                        ld hl, Results                   ; Apuntar al inicio del array de resultados
                        ld a, 9                          ; Longitud del array

SearchLoop:
                        ld b, (hl)                       ; Cargar elemento del array de resultados
                        cp b, 7                          ; Comparar con 7
                        jr z, FoundSeven                 ; Si es 7, terminar con 1
                        inc hl                           ; Siguiente elemento en el array de resultados
                        dec a                            ; Decrementar el contador
                        jr nz, SearchLoop                ; Repetir si no es 0

NotFoundSeven:
                        xor a                            ; Poner 0 en el acumulador (A)
                        jr EndProgram

FoundSeven:
                        ld a, 1                          ; Poner 1 en el acumulador (A)

EndProgram:
                        halt                             ; Fin del programa

AppLast                 equ *-1                          ; La dirección del último byte usado

; Genera algunos comandos útiles para depuración

                        profile AppFirst,AppLast-AppFirst+1     ; Habilita el perfilado para todo el código

; Configura los registros de emulación para que Zeus pueda emular este código correctamente

Zeus_PC                 equ AppFirst                            ; Indica al emulador dónde comenzar
Zeus_SP                 equ $FF40                               ; Indica al emulador dónde colocar la pila

; Estas líneas generan algunos archivos de salida

                        ; Genera un archivo SZX
                        output_szx AppFilename+".szx",$0000,AppFirst    ; El archivo SZX

                        ; Si queremos un cargador elegante, necesitamos cargar una pantalla de carga
;                        import_bin AppFilename+".scr",$4000            ; Cargar una pantalla de carga

                        ; Ahora, también genera un archivo TZX usando el cargador
                        output_tzx AppFilename+".tzx",AppFilename,"",AppFirst,AppLast-AppFirst,1,AppFirst ; Un archivo TZX usando el cargador
