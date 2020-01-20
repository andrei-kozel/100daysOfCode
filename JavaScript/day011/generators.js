function* WeaponGenerator() {
  yield "Katana";
  yield "Wakizashi";
}

const weaponsIterator = WeaponGenerator();

console.log("Weapon Iterator");
console.log(weaponsIterator);
console.log("1: ");
console.log(weaponsIterator.next());
console.log("2: ");
console.log(weaponsIterator.next());
console.log("3: ");
console.log(weaponsIterator.next());
