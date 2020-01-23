function Ninja() {}
Ninja.messgae = "Hello";
const ninja = new Ninja();
console.log(ninja.messgae);

function Ninja2() {}
Ninja2.prototype.talk = function() {
  return "Hello";
};
const ninja2 = new Ninja2();
console.log(ninja2.talk());

function Person() {}
function Ninja3() {}
const ninja3 = new Ninja3();
console.log(ninja3.constructor);
