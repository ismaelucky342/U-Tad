/** Flow Control */

let age = 20;

// If-else statement
if (age < 13) {
    console.log("You are a child.");
} else if (age >= 13 && age < 20) {
    console.log("You are a teenager.");
} else {
    console.log("You are an adult.");
}

// Switch statement
let day = 3;
let dayName;

switch (day) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid day";
}

console.log("Day " + day + " is " + dayName);

// For loop
console.log("For loop:");
for (let i = 1; i <= 5; i++) {
    console.log("Iteration " + i);
}

// While loop
console.log("While loop:");
let count = 1;
while (count <= 5) {
    console.log("Count " + count);
    count++;
}

// Do-while loop
console.log("Do-While loop:");
let num = 1;
do {
    console.log("Number " + num);
    num++;
} while (num <= 5);

// Break and continue
console.log("Break and Continue:");
for (let j = 1; j <= 10; j++) {
    if (j === 6) {
        console.log("Breaking the loop at " + j);
        break; // Exit loop when j is 6
    }
    if (j % 2 === 0) {
        console.log("Skipping even number " + j);
        continue; // Skip even numbers
    }
    console.log("Current number: " + j);
}

// Ternary operator
let isMember = true;
let discount = isMember ? 0.1 : 0.05;
console.log("Discount: " + (discount * 100) + "%");