const yoshi = { skulk: true };
const hattori = { sneak: true };
const kuma = { creep: true };

Object.setPrototypeOf(yoshi, hattori);
Object.setPrototypeOf(hattori, kuma);
console.log("yoshi -> hattori: " + yoshi.sneak);
console.log("yoshi -> kuma via hattori: " + yoshi.creep);
console.log("hattori -> yoshi: " + hattori.skulk);
