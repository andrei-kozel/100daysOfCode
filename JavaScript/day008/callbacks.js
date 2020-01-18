let text = "Domo arigato";
console.log("Before defining function!");

function useless(ninjaCallback) {
  console.log("In usless function");
  return ninjaCallback();
}

function getText() {
  console.log("In getText function");
  return text;
}

console.log("Before calls");
useless(getText);
console.log("After calls");
