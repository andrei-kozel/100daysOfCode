function Ninja(name) {
  this.name = name;
  this.skulk = function() {
    return this;
  };
}

let ninja1 = new Ninja("Ninja 1");
let ninja2 = new Ninja("Ninja 2");

console.log(ninja1.skulk());
console.log(ninja2.skulk());

function Ninja2() {
  this.skulk = function() {
    return true;
  };
  return 1;
}

let ninja21 = new Ninja2();

console.log(Ninja2());
console.log(ninja21);
console.log(ninja21.skulk());

console.log("---EMPEROR---");

let puppet = {
  rules: false
};

function Emperor() {
  this.rules = true;
  return puppet;
}

let emperor = new Emperor();

console.log(Emperor());
console.log(emperor);
console.log(emperor.rules);

console.log("----CAR----");
let bmw = {
  speed: 120,
  color: "red"
};

function Car() {
  this.spees = 10;
  this.color = "white";
  return bmw;
}

let smallCar = new Car();
console.log(smallCar);
