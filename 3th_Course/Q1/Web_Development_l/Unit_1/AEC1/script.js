// Juego del Ahorcado - JavaScript
class HangmanGame {
    constructor() {
        // Array de palabras para el juego
        this.words = [
            'JAVASCRIPT', 'PROGRAMACION', 'UNIVERSIDAD', 'ESTUDIANTE', 'PROYECTO',
            'DESARROLLO', 'APLICACION', 'TECNOLOGIA', 'ALGORITMO', 'FUNCION',
            'VARIABLE', 'BUCLE', 'CONDICIONAL', 'ARRAY', 'OBJETO',
            'CLASE', 'METODO', 'PROPIEDAD', 'EVENTO', 'INTERFAZ',
            'DISEÑO', 'CREATIVIDAD', 'INNOVACION', 'SOLUCION', 'PROBLEMA',
            'ANALISIS', 'PLANIFICACION', 'IMPLEMENTACION', 'PRUEBA', 'DEPURACION',
            'COMPUTADORA', 'SOFTWARE', 'HARDWARE', 'INTERNET', 'SERVIDOR',
            'CLIENTE', 'BASE', 'DATOS', 'CONSULTA', 'TABLA'
        ];
        
        // Estado del juego
        this.currentWord = '';
        this.guessedLetters = [];
        this.wrongGuesses = 0;
        this.maxWrongGuesses = 6;
        this.gameOver = false;
        this.gameWon = false;
        
        // Elementos del DOM
        this.wordDisplay = document.getElementById('word-display');
        this.letterInput = document.getElementById('letter-input');
        this.guessButton = document.getElementById('guess-button');
        this.restartButton = document.getElementById('restart-button');
        this.gameMessage = document.getElementById('game-message');
        this.attemptsLeft = document.getElementById('attempts-left');
        this.usedLetters = document.getElementById('used-letters');
        
        // Elementos del SVG del ahorcado
        this.hangmanParts = [
            document.getElementById('head'),
            document.getElementById('body'),
            document.getElementById('left-arm'),
            document.getElementById('right-arm'),
            document.getElementById('left-leg'),
            document.getElementById('right-leg')
        ];
        
        this.initializeGame();
        this.setupEventListeners();
    }
    
    // Requisito 1: Inicializar automáticamente la partida
    initializeGame() {
        // Reiniciar variables del juego
        this.currentWord = this.getRandomWord();
        this.guessedLetters = [];
        this.wrongGuesses = 0;
        this.gameOver = false;
        this.gameWon = false;
        
        // Reiniciar interfaz
        this.displayWord();
        this.updateHangman();
        this.updateAttemptsDisplay();
        this.updateUsedLetters();
        this.hideGameMessage();
        this.hideRestartButton();
        this.enableInput();
        
        // Enfocar el input
        this.letterInput.focus();
        
        console.log('Palabra secreta:', this.currentWord); // Para debug
    }
    
    // Obtener una palabra aleatoria del array
    getRandomWord() {
        const randomIndex = Math.floor(Math.random() * this.words.length);
        return this.words[randomIndex];
    }
    
    // Mostrar la palabra con huecos y letras adivinadas
    displayWord() {
        this.wordDisplay.innerHTML = '';
        
        for (let letter of this.currentWord) {
            const letterSlot = document.createElement('div');
            letterSlot.classList.add('letter-slot');
            
            if (this.guessedLetters.includes(letter)) {
                letterSlot.textContent = letter;
                letterSlot.classList.add('revealed');
            }
            
            this.wordDisplay.appendChild(letterSlot);
        }
    }
    
    // Configurar event listeners
    setupEventListeners() {
        // Requisito 2: Botón para realizar intento
        this.guessButton.addEventListener('click', () => this.makeGuess());
        
        // Permitir adivinar con Enter
        this.letterInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.makeGuess();
            }
        });
        
        // Requisito 4: Botón de reiniciar
        this.restartButton.addEventListener('click', () => this.initializeGame());
        
        // Validar entrada solo letras
        this.letterInput.addEventListener('input', (e) => {
            const value = e.target.value.toUpperCase();
            const validValue = value.replace(/[^A-ZÁÉÍÓÚÑÜ]/g, '');
            e.target.value = validValue;
        });
    }
    
    // Requisito 2 y 3: Realizar intento de adivinar
    makeGuess() {
        const letter = this.letterInput.value.toUpperCase().trim();
        
        // Validar que se introduce únicamente una letra
        if (!letter) {
            this.showError('Por favor, introduce una letra');
            return;
        }
        
        if (letter.length !== 1) {
            this.showError('Introduce solo una letra');
            return;
        }
        
        if (!/^[A-ZÁÉÍÓÚÑÜ]$/.test(letter)) {
            this.showError('Introduce solo letras válidas');
            return;
        }
        
        // Verificar si la letra ya fue utilizada
        if (this.guessedLetters.includes(letter)) {
            this.showError('Ya has usado esta letra');
            return;
        }
        
        // Añadir letra a las utilizadas
        this.guessedLetters.push(letter);
        
        // Verificar si la letra está en la palabra
        if (this.currentWord.includes(letter)) {
            this.handleCorrectGuess(letter);
        } else {
            this.handleWrongGuess(letter);
        }
        
        // Limpiar input
        this.letterInput.value = '';
        
        // Actualizar displays
        this.updateUsedLetters();
        this.displayWord();
        
        // Verificar estado del juego
        this.checkGameState();
    }
    
    // Manejar acierto
    handleCorrectGuess(letter) {
        // Añadir efecto visual positivo
        this.wordDisplay.style.animation = 'none';
        setTimeout(() => {
            this.wordDisplay.style.animation = 'fadeIn 0.5s ease';
        }, 10);
    }
    
    // Manejar error
    handleWrongGuess(letter) {
        this.wrongGuesses++;
        this.updateHangman();
        this.updateAttemptsDisplay();
        
        // Añadir efecto visual de error
        this.letterInput.classList.add('shake');
        setTimeout(() => {
            this.letterInput.classList.remove('shake');
        }, 500);
    }
    
    // Requisito 3: Verificar estado del juego (victoria o derrota)
    checkGameState() {
        // Verificar victoria
        const wordLetters = [...new Set(this.currentWord)]; // Letras únicas de la palabra
        const guessedWordLetters = wordLetters.filter(letter => 
            this.guessedLetters.includes(letter)
        );
        
        if (guessedWordLetters.length === wordLetters.length) {
            this.gameWon = true;
            this.gameOver = true;
            this.showVictory();
            return;
        }
        
        // Verificar derrota
        if (this.wrongGuesses >= this.maxWrongGuesses) {
            this.gameOver = true;
            this.showDefeat();
            return;
        }
    }
    
    // Mostrar mensaje de victoria
    showVictory() {
        this.gameMessage.textContent = '¡Felicidades! Has ganado la partida';
        this.gameMessage.className = 'game-message victory';
        this.showRestartButton();
        this.disableInput();
    }
    
    // Mostrar mensaje de derrota
    showDefeat() {
        this.gameMessage.textContent = `Has perdido. La palabra era: ${this.currentWord}`;
        this.gameMessage.className = 'game-message defeat';
        this.showRestartButton();
        this.disableInput();
    }
    
    // Mostrar error temporal
    showError(message) {
        this.gameMessage.textContent = message;
        this.gameMessage.className = 'game-message defeat';
        
        // Ocultar mensaje después de 2 segundos
        setTimeout(() => {
            if (this.gameMessage.textContent === message) {
                this.hideGameMessage();
            }
        }, 2000);
    }
    
    // Actualizar dibujo del ahorcado
    updateHangman() {
        // Mostrar partes del cuerpo según errores cometidos
        for (let i = 0; i < this.wrongGuesses && i < this.hangmanParts.length; i++) {
            if (this.hangmanParts[i]) {
                this.hangmanParts[i].style.display = 'block';
            }
        }
        
        // Ocultar partes restantes
        for (let i = this.wrongGuesses; i < this.hangmanParts.length; i++) {
            if (this.hangmanParts[i]) {
                this.hangmanParts[i].style.display = 'none';
            }
        }
    }
    
    // Actualizar contador de intentos
    updateAttemptsDisplay() {
        const attemptsRemaining = this.maxWrongGuesses - this.wrongGuesses;
        this.attemptsLeft.textContent = attemptsRemaining;
        
        // Cambiar color según intentos restantes
        if (attemptsRemaining <= 2) {
            this.attemptsLeft.style.color = '#e74c3c';
        } else if (attemptsRemaining <= 4) {
            this.attemptsLeft.style.color = '#f39c12';
        } else {
            this.attemptsLeft.style.color = '#27ae60';
        }
    }
    
    // Actualizar letras utilizadas
    updateUsedLetters() {
        this.usedLetters.textContent = this.guessedLetters.join(' ');
    }
    
    // Funciones de interfaz
    showRestartButton() {
        this.restartButton.style.display = 'block';
    }
    
    hideRestartButton() {
        this.restartButton.style.display = 'none';
    }
    
    hideGameMessage() {
        this.gameMessage.textContent = '';
        this.gameMessage.className = 'game-message';
    }
    
    enableInput() {
        this.letterInput.disabled = false;
        this.guessButton.disabled = false;
        this.letterInput.focus();
    }
    
    disableInput() {
        this.letterInput.disabled = true;
        this.guessButton.disabled = true;
    }
}

// Requisito 1: Iniciar automáticamente cuando se carga la página
document.addEventListener('DOMContentLoaded', () => {
    new HangmanGame();
});