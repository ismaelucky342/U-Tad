//====================================================================================================#
//      AEC1 - Desarrollo Web I                    Ismael Hernandez Clemente                         #
//      Juego del Ahorcado                         ismael.hernandez@live.u-tad.com                   #
//====================================================================================================#

class HangmanGame {
    constructor() {
        this.currentWord = '';
        this.guessedLetters = [];
        this.wrongGuesses = 0;
        this.gameOver = false;
        
        // Referencias DOM
        this.wordDisplay = document.getElementById('word-display');
        this.letterInput = document.getElementById('letter-input');
        this.guessButton = document.getElementById('guess-button');
        this.restartButton = document.getElementById('restart-button');
        this.gameMessage = document.getElementById('game-message');
        this.attemptsLeft = document.getElementById('attempts-left');
        this.usedLetters = document.getElementById('used-letters');
        this.hangmanParts = [
            document.getElementById('head'),
            document.getElementById('hangman-body'),
            document.getElementById('left-arm'),
            document.getElementById('right-arm'),
            document.getElementById('left-leg'),
            document.getElementById('right-leg')
        ];
        
        this.init();
        this.setupEvents();
    }
    
    // Requisito 1: Inicio automático
    init() {
        this.currentWord = getRandomWord();
        this.guessedLetters = [];
        this.wrongGuesses = 0;
        this.gameOver = false;
        
        this.displayWord();
        this.updateHangman();
        this.attemptsLeft.textContent = GAME_CONFIG.MAX_WRONG_GUESSES;
        this.usedLetters.textContent = '';
        this.gameMessage.textContent = '';
        this.gameMessage.className = 'game-message';
        this.restartButton.style.display = 'none';
        this.letterInput.disabled = false;
        this.guessButton.disabled = false;
        this.letterInput.value = '';
        this.letterInput.focus();
    }
    
    setupEvents() {
        // Requisito 2: Botón adivinar
        this.guessButton.addEventListener('click', () => this.makeGuess());
        this.letterInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.makeGuess();
        });
        
        // Requisito 4: Botón reiniciar
        this.restartButton.addEventListener('click', () => this.init());
        
        // Validación de input
        this.letterInput.addEventListener('input', (e) => {
            e.target.value = e.target.value.toUpperCase().replace(/[^A-ZÁÉÍÓÚÑÜ]/g, '');
        });
    }
    
    displayWord() {
        this.wordDisplay.innerHTML = '';
        for (let letter of this.currentWord) {
            const slot = document.createElement('div');
            slot.classList.add('letter-slot');
            if (this.guessedLetters.includes(letter)) {
                slot.textContent = letter;
                slot.classList.add('revealed');
            }
            this.wordDisplay.appendChild(slot);
        }
    }
    
    // Requisito 2 y 3: Lógica de intento
    makeGuess() {
        const letter = this.letterInput.value.toUpperCase().trim();
        
        if (!letter || letter.length !== 1) {
            this.showError('Introduce una letra');
            return;
        }
        
        if (!isValidLetter(letter)) {
            this.showError('Letra no válida');
            return;
        }
        
        if (this.guessedLetters.includes(letter)) {
            this.showError('Letra ya usada');
            return;
        }
        
        this.guessedLetters.push(letter);
        this.letterInput.value = '';
        
        if (!this.currentWord.includes(letter)) {
            this.wrongGuesses++;
            this.updateHangman();
            this.letterInput.classList.add('shake');
            setTimeout(() => this.letterInput.classList.remove('shake'), 500);
        }
        
        this.displayWord();
        this.usedLetters.textContent = this.guessedLetters.join(' ');
        this.attemptsLeft.textContent = GAME_CONFIG.MAX_WRONG_GUESSES - this.wrongGuesses;
        this.checkGameState();
    }
    
    // Requisito 3: Verificación de victoria/derrota
    checkGameState() {
        const wordLetters = [...new Set(this.currentWord)];
        const allGuessed = wordLetters.every(l => this.guessedLetters.includes(l));
        
        if (allGuessed) {
            this.gameMessage.textContent = '¡Felicidades! Has ganado';
            this.gameMessage.className = 'game-message victory';
            this.endGame();
        } else if (this.wrongGuesses >= GAME_CONFIG.MAX_WRONG_GUESSES) {
            this.gameMessage.textContent = `Has perdido. Era: ${this.currentWord}`;
            this.gameMessage.className = 'game-message defeat';
            this.endGame();
        }
    }
    
    updateHangman() {
        this.hangmanParts.forEach((part, i) => {
            if (part) part.style.display = i < this.wrongGuesses ? 'block' : 'none';
        });
    }
    
    showError(msg) {
        this.gameMessage.textContent = msg;
        this.gameMessage.className = 'game-message defeat';
        setTimeout(() => {
            if (this.gameMessage.textContent === msg) {
                this.gameMessage.textContent = '';
            }
        }, GAME_CONFIG.ERROR_MESSAGE_DURATION);
    }
    
    endGame() {
        this.letterInput.disabled = true;
        this.guessButton.disabled = true;
        this.restartButton.style.display = 'block';
    }
}

// Requisito 1: Auto-inicio
document.addEventListener('DOMContentLoaded', () => new HangmanGame());
