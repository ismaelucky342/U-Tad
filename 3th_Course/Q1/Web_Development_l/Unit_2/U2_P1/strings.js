/*come with me and you will be
in a world of fcking strings*/

let string1 = "Hello, ";
let string2 = 'world!';
let string3 = `This is a template literal.`;

console.log(string1 + string2); // Concatenation
console.log(string3);

let name = "Bob";
let age = 25;
let greeting = `My name is ${name} and I am ${age} years old.`;

console.log(greeting);

// String methods
let sampleString = "  JavaScript is awesome!  ";

console.log(sampleString.length); // Length of the string
console.log(sampleString.toUpperCase()); // Uppercase
console.log(sampleString.toLowerCase()); // Lowercase
console.log(sampleString.trim()); // Remove whitespace
console.log(sampleString.includes("awesome")); // Check substring
console.log(sampleString.indexOf("is")); // Find index of substring
console.log(sampleString.slice(2, 14)); // Extract substring


// Escape characters
let escapeString = "He said, \"JavaScript is fun!\"\nLet's code.";
console.log(escapeString);

// Multiline string using template literals
let multiLineString = `This is line one.
This is line two.
This is line three.`;

console.log(multiLineString);  


// String comparison
let strA = "apple";
let strB = "banana";

console.log(strA === strB); // Equality
console.log(strA < strB); // Lexicographical comparison

