; Definición de los arrays y las variables
ORG 32768

ARRAY1:  DB 1,2,3,4,5,6,7,8,9
ARRAY2:  DB 2,2,1,1,1,9,1,1,1
RESULTS: DS 9 ; Array vacío para resultados

; Punteros y contadores
LD HL, ARRAY1    ; HL apunta al inicio de ARRAY1
LD DE, ARRAY2    ; DE apunta al inicio de ARRAY2
LD IX, RESULTS   ; IX apunta al inicio de RESULTS
LD B, 9          ; Tamaño de los arrays (contador de elementos)
LD C, 0          ; Índice para iteración

; Inicio del bucle principal
MAIN_LOOP:
    LD A, (HL)   ; Cargar elemento de ARRAY1
    LD D, (DE)   ; Cargar elemento de ARRAY2 en D

    CP D         ; Comparar A con D (elemento actual de ARRAY2)
    JR Z, EQUAL  ; Si son iguales, ir a la etiqueta EQUAL

    JR C, LESS   ; Si A < D, ir a la etiqueta LESS
    JR GREATER   ; Si A > D, ir a la etiqueta GREATER

EQUAL:
    LD A, 7      ; Si son iguales, almacenar 7 en el array de resultados
    JR STORE_RESULT

LESS:
    LD A, D      ; A = elemento de ARRAY2
    SUB (HL)     ; Restar elemento de ARRAY1 de A
    JR STORE_RESULT

GREATER:
    LD A, (HL)   ; Restaurar A (elemento de ARRAY1)
    ADD A, D     ; Sumar elemento de ARRAY2 a A

STORE_RESULT:
    LD (IX+C), A ; Guardar resultado en el array de resultados
    INC HL       ; Incrementar puntero de ARRAY1
    INC DE       ; Incrementar puntero de ARRAY2
    INC C        ; Incrementar índice del array de resultados
    DJNZ MAIN_LOOP ; Si no hemos terminado, repetir el bucle principal

; Buscar el valor 7 en el array de resultados
LD HL, RESULTS   ; Reiniciar HL al inicio del array de resultados
LD A, 0          ; A = 0 (indicador de no encontrado)
LD B, 9          ; Reiniciar contador

SEARCH_LOOP:
    LD A, (HL)   ; Cargar elemento actual de RESULTS
    CP 7         ; Comparar con 7
    JR Z, FOUND  ; Si encontramos un 7, ir a la etiqueta FOUND
    INC HL       ; Incrementar puntero de RESULTS
    DJNZ SEARCH_LOOP ; Si no hemos terminado, repetir el bucle de búsqueda

NOT_FOUND:
    LD A, 0      ; Si no se encuentra 7, A = 0
    JR END       ; Ir al final del programa

FOUND:
    LD A, 1      ; Si se encuentra 7, A = 1

END:
    NOP          ; No hacer nada, puede ser un punto de interrupción para depuración
    RET          ; Terminar el programa

