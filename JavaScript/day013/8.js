// class Warrior {
//   constructor(weapon) {
//     this.weapon = weapon;
//   }
//   wield() {
//     return "Wielding " + this.weapon;
//   }
//   static duel(warrior1, warrior2) {
//     return warrior1.wield() + " " + warrior2.wield();
//   }
// }

function Warrior(weapon) {
  this.weapon = weapon;
}

Warrior.prototype.wield = function() {
  return "Wielding " + this.weapon;
};

Warrior.duel = function(warrior1, warrior2) {
  return warrior1.wield() + " " + warrior2.wield();
};

let warrior1 = new Warrior("Knife");
let warrior2 = new Warrior("Sword");

console.log(warrior1.wield());
console.log(warrior2.wield());

console.log(Warrior.duel(warrior1, warrior2));
