// my answers in comments
// 1
/*

a1 = 2
a2 = 4
a3 = 2
a4 = 6

*/

function* EvenGenerator() {
  let num = 2;
  while (true) {
    yield num;
    num = num + 2;
  }
}

let generator = EvenGenerator();

let a1 = generator.next().value;
let a2 = generator.next().value;
let a3 = EvenGenerator().next().value;
let a4 = generator.next().value;
console.log("a1: " + a1);
console.log("a2: " + a2);
console.log("a3: " + a3);
console.log("a4: " + a4);
