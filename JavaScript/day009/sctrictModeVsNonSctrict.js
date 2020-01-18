function nonStrictMode() {
  return this;
}

function strictMode() {
  "use strict";
  return this;
}

console.log(nonStrictMode());
console.log(strictMode());

function whatIsMyContext() {
  return this;
}

let person = {
  name: "Andrei",
  age: "99",
  context: whatIsMyContext
};

let person2 = {
  name: "Margaret",
  age: "99",
  context: whatIsMyContext
};

console.log(person.context());
console.log(person2.context());
