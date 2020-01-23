// 1. ['Oda', 'Tomoe', empty, ''Hattori]
const samurai = ["Oda", "Tomoe"];
samurai[3] = "Hattori";
console.log(samurai);

// 2. ['Hattori', 'Yoshi']
const ninjas = [];
ninjas.push("Yoshi");
ninjas.unshift("Hattori");
ninjas.length = 3;
ninjas.pop();
console.log(ninjas);

// 3. Tomoe, Hattori, Takeda
const samurai2 = [];
samurai2.push("Oda");
samurai2.unshift("Tomoe");
samurai2.splice(1, 0, "Hattori", "Takeda");
samurai2.pop();
console.log(samurai2);

// 4. 57
const ninjas2 = [
  { name: "Yoshi", age: 18 },
  { name: "Hattori", age: 19 },
  { name: "Yagyu", age: 20 }
];
const first = ninjas2.map(ninja => ninja.age);
const second = first.filter(age => age % 2 == 0);
const third = first.reduce((aggregate, item) => aggregate + item, 0);
console.log(first);
console.log(second);
console.log(third);
