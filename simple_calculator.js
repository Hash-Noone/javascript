const prompt = require("prompt-sync")();

console.log("This is a simple calculator");

let result = 0;
let stack = [];

while (true) {

    const operator = prompt(
        "Enter your operator (+, -, *, /), undo, or exit: "
    ).trim();

    if (operator === "exit") {
        break;
    }

    if (operator === "undo") {

        if (stack.length > 0) {
            result = stack.pop();
            console.log(`Result: ${result}`);
        } else {
            console.log("Nothing to undo");
        }

        continue;
    }

    const input = prompt("Enter the operand: ").trim();
    const secondNumber = Number(input);

    if (Number.isNaN(secondNumber)) {
        console.log("Please enter a valid number.");
        continue;
    }

    const prev = result;

    switch (operator) {

        case "+":
            result += secondNumber;
            break;

        case "-":
            result -= secondNumber;
            break;

        case "*":
            result *= secondNumber;
            break;

        case "/":
            if (secondNumber === 0) {
                console.log("Can't divide by zero");
                continue;
            }

            result /= secondNumber;
            break;

        default:
            console.log("Invalid operator.");
            continue;
    }

    stack.push(prev);

    console.log(`Result: ${result}`);
}