class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  getName() {
    return this.name;
  }

  getAge() {
    return this.age;
  }

  setName(name) {
    this.name = name;
  }

  setAge(age) {
    this.age = age;
  }
}

class Gamer extends Person {
  constructor(name, age, games) {
    super(name, age);
    this.games = games;
  }

  getGames() {
    return this.games;
  }

  setGame(game) {
    this.games.push(game);
  }
}

let gamer1 = new Gamer("Dendi", 34, ["Dota 2", "CS GO"]);
console.log(gamer1.getName());
console.log(gamer1.getAge());
console.log(gamer1.getGames());
