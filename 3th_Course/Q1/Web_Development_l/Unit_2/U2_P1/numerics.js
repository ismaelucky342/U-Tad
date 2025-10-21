/*numerical operations */

export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

export function multiply(a, b) {
    return a * b;
}

export function divide(a, b) {
    if (b === 0) {
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}

export function modules(a ,b){
    return a % b; 
}

export function power(a, b){
    return Math.pow(a, b);
}

export function sqrt(a){
    return Math.sqrt(a);
}

export function isEven(a){
    return a % 2 === 0;
}

export function isOdd(a){
    return a % 2 !== 0;
}