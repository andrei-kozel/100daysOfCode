function Person() {
  this.context = function() {
    return this;
  };
}

let person = new Person();

console.log("person: " + person);
console.log("person.context(): " + person.context());
console.log("person.context: " + person.context);
console.log("Person(): " + Person());
console.log();
console.log();

console.log("------------------------------");
console.log("APPLY AND CALL METHODS");
console.log("------------------------------");

// apply and call methods
function sum() {
  let result = 0;
  for (let i = 0; i < arguments.length; i++) {
    result += arguments[i];
  }
  // puts the result onto whatever object
  // is the function context
  console.log(this);
  this.result = result;
}

let sum1 = { name: "sum1" };
let sum2 = { name: "sum2" };

sum.apply(sum1, [1, 2, 2, 3, 4, 5, 6]);
sum.call(sum2, 1, 1, 22, 3, 4, 5, 6, 9);

console.log("sum1 result: " + sum1.result);
console.log("sum2 result: " + sum2.result);

console.log();
console.log();
console.log("------------------------------");
console.log("ARROW FUNCTION AND THIS + BIND");
console.log("------------------------------");

function Button() {
  this.clicked = false;
  this.click = function() {
    this.clicked = true;
    console.log(button.clicked);
    console.log(this);
    return this;
  };
}

function Button2() {
  this.clicked = false;
  this.click = () => {
    this.clicked = true;
    console.log(button2.clicked);
    console.log(this);
    return this;
  };
}

let button = new Button();
let button2 = new Button2();

document
  .querySelector("#button")
  .addEventListener("click", button.click.bind(button));

document.querySelector("#button2").addEventListener("click", button2.click);
