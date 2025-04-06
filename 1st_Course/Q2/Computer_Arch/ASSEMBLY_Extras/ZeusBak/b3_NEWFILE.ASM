; Definición de los arrays y las variables
ORG 32768

ARRAY1:  DB 1,2,3,4,5,6,7,8,9
ARRAY2:  DB 2,2,1,1,1,9,1,1,1
RESULTS: DS 9 ; Array vacío para resultados

; Punteros y contadores
LD HL, ARRAY1    ; HL apunta al inicio de ARRAY1
LD DE, ARRAY2    ; DE apunta al inicio de ARRAY2
LD BC, RESULTS   ; BC apunta al inicio de RESULTS
LD A, 9          ; Tamaño de los arrays (contador de elementos)
LD IX, 0         ; Índice para iteración

; Inicio del bucle principal
MAIN_LOOP:
    LD A, (HL)   ; Cargar elemento de ARRAY1
    LD L, (DE)   ; Cargar elemento de ARRAY2 en L

    CP L         ; Comparar A con L (elemento actual de ARRAY2)
    JR Z, EQUAL  ; Si son iguales, ir a la etiqueta EQUAL

    JR C, LESS   ; Si A < L, ir a la etiqueta LESS
    JR GREATER   ; Si A > L, ir a la etiqueta GREATER

EQUAL:
    LD A, 7      ; Si son iguales, almacenar 7 en el array de resultados
    JR STORE_RESULT

LESS:
    LD A, (DE)   ; A = elemento de ARRAY2
    SUB (HL)     ; Restar elemento de ARRAY1 de A
    JR STORE_RESULT

GREATER:
    ADD A, (DE)  ; Sumar elemento de ARRAY2 a A

STORE_RESULT:
    LD (BC), A   ; Guardar resultado en el array de resultados
    INC HL       ; Incrementar puntero de ARRAY1
    INC DE       ; Incrementar puntero de ARRAY2
    INC BC       ; Incrementar puntero del array de resultados
    DEC IX       ; Incrementar índice de iteración
    CP IX        ; Comparar índice con tamaño del array
    JR NZ, MAIN_LOOP ; Si no hemos terminado, repetir el bucle principal

; Buscar el valor 7 en el array de resultados
LD HL, RESULTS   ; Reiniciar HL al inicio del array de resultados
LD A, 0          ; A = 0 (indicador de no encontrado)
LD IX, 9         ; Reiniciar contador

SEARCH_LOOP:
    LD A, (HL)   ; Cargar elemento actual de RESULTS
    CP 7         ; Comparar con 7
    JR Z, FOUND  ; Si encontramos un 7, ir a la etiqueta FOUND
    INC HL       ; Incrementar puntero de RESULTS
    DEC IX       ; Decrementar contador
    JR NZ, SEARCH_LOOP ; Si no hemos terminado, repetir el bucle de búsqueda

NOT_FOUND:
    LD A, 0      ; Si no se encuentra 7, A = 0
    JR END       ; Ir al final del programa

FOUND:
    LD A, 1      ; Si se encuentra 7, A = 1

END:
    NOP          ; No hacer nada, puede ser un punto de interrupción para depuración
    RET          ; Terminar el programa

