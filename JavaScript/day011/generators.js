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

function* NinjaGenerator(action) {
  const imposter = yield "Hattori " + action;
  console.log(imposter);

  yield "Yoshi (" + imposter + ") " + action;
}

const ninjaIterator = NinjaGenerator("skulk");

const result1 = ninjaIterator.next();
const result2 = ninjaIterator.next("Hanzo");

console.log(result1);
console.log(result2);
