const prompt = require("prompt-sync")();

console.log("This is a number guessing game");

const targetNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
const maxAttempts = 10;

while (attempts < maxAttempts) {

    const input = prompt("What is your guess between 1 and 100? ");
    const userGuess = Number(input);

    if (Number.isNaN(userGuess)) {
        console.log("Please enter a valid number.");
        continue;
    }

    attempts++;

    if (userGuess === targetNumber) {
        console.log(`Correct! You got it in ${attempts} ${attempts === 1 ? "try" : "tries"}.`);
        break;
    }

    if (userGuess < targetNumber) {
        console.log(`Your guess is lower. ${attempts} ${attempts === 1 ? "try" : "tries"} used.`);
    } else {
        console.log(`Your guess is higher. ${attempts} ${attempts === 1 ? "try" : "tries"} used.`);
    }

    if (attempts === maxAttempts) {
        console.log(`Game over! The number was ${targetNumber}.`);
    }
}