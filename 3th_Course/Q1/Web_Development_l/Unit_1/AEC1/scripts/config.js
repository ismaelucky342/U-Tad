//====================================================================================================#
//      AEC1 - Desarrollo Web I                    Ismael Hernandez Clemente                         #
//      Juego del Ahorcado                         ismael.hernandez@live.u-tad.com                   #
//====================================================================================================#

const GAME_CONFIG = {
    WORDS: [
        'JAVASCRIPT', 'PROGRAMACION', 'UNIVERSIDAD', 'ESTUDIANTE', 'PROYECTO',
        'DESARROLLO', 'APLICACION', 'TECNOLOGIA', 'ALGORITMO', 'FUNCION',
        'VARIABLE', 'BUCLE', 'CONDICIONAL', 'ARRAY', 'OBJETO',
        'CLASE', 'METODO', 'PROPIEDAD', 'EVENTO', 'INTERFAZ',
        'DISEÑO', 'CREATIVIDAD', 'INNOVACION', 'SOLUCION', 'PROBLEMA',
        'ANALISIS', 'PLANIFICACION', 'IMPLEMENTACION', 'PRUEBA', 'DEPURACION',
        'COMPUTADORA', 'SOFTWARE', 'HARDWARE', 'INTERNET', 'SERVIDOR',
        'CLIENTE', 'BASE', 'DATOS', 'CONSULTA', 'TABLA'
    ],
    MAX_WRONG_GUESSES: 6,
    ERROR_MESSAGE_DURATION: 2000
};

function getRandomWord() {
    return GAME_CONFIG.WORDS[Math.floor(Math.random() * GAME_CONFIG.WORDS.length)];
}

function isValidLetter(char) {
    return /^[A-ZÁÉÍÓÚÑÜ]$/.test(char);
}
