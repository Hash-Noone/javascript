const word = "A man, a plan, a canal: Panama";

const cleaned = word
    .replace(/[^a-zA-Z0-9]/g, "")
    .toLowerCase();

// const reversed = cleaned.split("").reverse().join("")

// console.log(cleaned === reversed)
let isPalindrome = true;


let j = cleaned.length - 1;
const len = Math.floor(cleaned.length/2)
for (let char of cleaned.slice(0,len)) {
    if (char != cleaned[j]) {
        isPalindrome = false;
        break;
    }
    j--;
} 
if (isPalindrome) {
    console.log("true");
} else {
    console.log("false");
}