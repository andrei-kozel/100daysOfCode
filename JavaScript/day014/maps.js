// dont use. For test purpose

const first = document.querySelector(".first");
const second = document.querySelector(".second");
const map = {};

map[first] = { data: "first" };
console.log(map);

map[second] = { data: "second" };
console.log(map);

console.log(map[first].data);

// creating map
const ninjaIslandMap = new Map();

const ninja1 = { name: "Yoshi" };
const ninja2 = { name: "Hattori" };
const ninja3 = { name: "Kuma" };

ninjaIslandMap.set(ninja1, { homeIsland: "Honshu" });
ninjaIslandMap.set(ninja2, { homeIsland: "Hokkaido" });

console.log(ninjaIslandMap);
console.log(ninjaIslandMap.has(ninja1));
